from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.db.models import Q
from watson_developer_cloud import LanguageTranslatorV3
import json
from .models import Movie
from .forms import MovieForm

from .models import Movie, Imdb_movie
from .forms import UserForm

import requests

now = timezone.now()

# Create your views here.

def home(request):
    movie_list = Movie.objects.all()
    return render(request, 'app/home.html', {
        'movie_list': movie_list,
    })

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


# Static Pages
# ---------------------------------------
def About(request):
    return render(request, 'About.html')

def Contact(request):
 return render(request,'Contact.html')


