from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import date, timedelta
from django.db.models import Q
from watson_developer_cloud import LanguageTranslatorV3
import json
from .models import Category, Product, Movie
from .forms import MovieForm
from datetime import date

from .models import Movie, Imdb_movie, Box_Office
from .forms import UserForm
from cart.forms import CartAddProductForm

import requests

# imports for API calls
from rest_framework import status
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from .serializers import *
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

now = timezone.now()

# Create your views here.

def home(request):
    movie_list = Movie.objects.all()
    box_office_check()
    box_office = Box_Office.objects.all()

    print('>> Box office Movies loaded - ' + str(box_office.count()))
    return render(request, 'app/home.html', {
        'movie_list': movie_list,
        'box_office': box_office,
    })

# Box Office Views

def box_office_check():
    print('>>> Checking if Box office needs a refresh')
    first_movie = Box_Office.objects.first()
    if first_movie:
        print('>>> Movie list present')
        if date.today() - first_movie.refreshed_date > timedelta(days=3):
            box_office_refresh()
    else:
        box_office_refresh()
            

def box_office_refresh():
    print('>>> Performing box office refresh')
    Box_Office.objects.all().delete()
    url = 'https://uflixit.p.rapidapi.com/movies/boxoffice' 
    headers = {
        'X-RapidAPI-Host': "uflixit.p.rapidapi.com",
        'X-RapidAPI-Key': "fb54a2a79amshb032c359722438fp18abb9jsn80dd3fd3790f",
    }
    json_data = requests.get(url, headers = headers).json()
    counter = 0
    for result in json_data['result']:
        if counter > 4:
            break
        add_box_office_movie(result)
        counter += 1

def add_box_office_movie(imdb_id):
    url = 'https://movie-database-imdb-alternative.p.rapidapi.com/' 
    params = {
        'i': imdb_id,
        'r': 'json',
    }
    headers = {
        'X-RapidAPI-Host': "movie-database-imdb-alternative.p.rapidapi.com",
        'X-RapidAPI-Key': "fb54a2a79amshb032c359722438fp18abb9jsn80dd3fd3790f",
    }
    movie = requests.get(url, params = params, headers = headers).json()
    # Create a Box Office Movie Object
    bo = Box_Office()
    bo.imdb_id = imdb_id
    bo.movie_name = movie['Title']
    bo.poster = movie['Poster']
    bo.refreshed_date = date.today()
    bo.save()

# Auth Views

def signup(request):
    if request.method=="POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user.set_password(password)
            user.save()
            user = authenticate(username=username, password=password)
            login(request, user)
            return render(request, 'app/home.html')
    else:
        form = UserForm()
    return render(request, 'registration/signup.html', {'form': form})


# Movie Views
def movie_list(request):
    movie_list = Movie.objects.all()
    return render(request, 'app/movie_list.html', {
        'movie_list': movie_list,
    })

@login_required
def movie_edit(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == "POST":
       # update
       form = MovieForm(request.POST, instance=movie)
       if form.is_valid():
            movie = form.save(commit=False)
            movie.updated_date = timezone.now()
            movie.save()
            return redirect('app:movie_detail', pk=pk)
    else:
        # edit
       form = MovieForm(instance=movie)
    return render(request, 'app/movie_edit.html', {'form': form})

@login_required
def movie_delete(request, pk):
   movie = get_object_or_404(Movie, pk=pk)
   movie.delete()
   return redirect('app:movie_list')

@login_required
def movie_new(request):
   if request.method == "POST":
       form = MovieForm(request.POST)
       if form.is_valid():
           movie = form.save(commit=False)
           movie.created_date = timezone.now()
           movie.save()
           movie_list = Movie.objects.all()
           return render(request, 'app/movie_list.html',
                         {'movie_list': movie_list})
   else:
       form = MovieForm()
       # print("Else")
   return render(request, 'app/movie_new.html', {'form': form})

language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    iam_apikey='8aBDAhLIsZ_v4LcakmqYOMyP2nWhKAUGrTR6KZE71Ic3')

def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    translation = language_translator.translate(
        text=movie.review, model_id='en-es').get_result()
    obj = (json.dumps(translation, indent=2, ensure_ascii=False))
    print(obj)
    obj2 = json.loads(obj)
    movie.obj2 = obj2['translations'][0]['translation']
    imovie = Imdb_movie(movie.imdb_id)
    return render(request, 'app/movie_detail.html', {
        'movie': movie,
        'imdb_movie': imovie,
    })

def imdb_movie_detail(request, pk):
    url = 'https://movie-database-imdb-alternative.p.rapidapi.com/' 
    params = {
        'i': pk,
        'r': 'json',
    }
    headers = {
        'X-RapidAPI-Host': "movie-database-imdb-alternative.p.rapidapi.com",
        'X-RapidAPI-Key': "fb54a2a79amshb032c359722438fp18abb9jsn80dd3fd3790f",
    }
    movie = requests.get(url, params = params, headers = headers).json()
    return render(request, 'app/imdb_movie_detail.html', {
        'movie': movie,
    })

def movie_nearby(request):
    if request.method == "GET":
        zip = request.GET.get('zipcode').strip()
        if zip:
            today = date.today().strftime('%Y-%m-%d')
            print(today)
            url = 'http://data.tmsapi.com/v1.1/movies/showings' 
            params = {
                'zip': zip,
                'startDate': today,
                'api_key': 'uw3r8cvvnpcyhqkw6mvu8jah'
            }

            showtimes = requests.get(url, params = params).json()
            print('>>> API call: ')
            return render(request, 'app/movie_nearby.html', {
                'showtimes': showtimes,
                'zipcode': zip,
            })
        else:
            print('Empty Zip')


# Movie Search
# --------------------------------------------
def search_imdb(search_string):
    url = 'https://movie-database-imdb-alternative.p.rapidapi.com/' 
    params = {
        'page': '1',
        's': search_string,
        'r': 'json',
        'type': 'movie',
    }
    headers = {
        'X-RapidAPI-Host': "movie-database-imdb-alternative.p.rapidapi.com",
        'X-RapidAPI-Key': "fb54a2a79amshb032c359722438fp18abb9jsn80dd3fd3790f",
    }
    json_data = requests.get(url, params = params, headers = headers).json()
    # for result in json_data['Search']:
    #     print(result['Title'], result['Year'], result['imdbID'], sep=', ')
    return json_data

def movie_search(request):
    movie_list = Movie.objects.all()
    if(request.method == 'GET'):
        search_string = request.GET.get('moviename').strip()
        if search_string:
            movie_list = Movie.objects.filter(Q(name__icontains=search_string))
            imdb_movie_list = search_imdb(search_string)
            return render(request, 'app/movie_list.html', {
                'movie_list': movie_list,
                'imdb_movie_list': imdb_movie_list,
                'result_has_imdb_result': True,
            })
       
    return render(request, 'app/movie_list.html',{
                'movie_list': movie_list,
    })

#------------------------------
# Shop Code

@login_required()
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,'shop/product/list.html',
                    {'category': category,
                    'categories': categories,
                    'products': products})

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug,available=True)
    cart_product_form = CartAddProductForm()
    return render(request,'shop/product/detail.html',{'product': product,
                                                       'cart_product_form': cart_product_form})


#----------------------------------------


# Static Pages
# ---------------------------------------
def About(request):
    return render(request, 'About.html')

def Contact(request):
 return render(request,'Contact.html')


# REST API Expose
# -----------------

@csrf_exempt
@api_view(['GET', 'POST'])
def movie_list_rest(request):
    permission_classes = (IsAuthenticatedOrReadOnly)
    if request.method == 'GET':
        movie_list = Movie.objects.all()
        serializer = MovieSerializer(movie_list, context={'request': request}, many=True)
        return Response({'data': serializer.data})
    
    elif request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def get_movie_rest(request, pk):
    # Retrieve, update or delete a movie instance.
    try:
        movie = Movie.objects.get(imdb_id=pk)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MovieSerializer(movie,context={'request': request})
        return Response(serializer.data)