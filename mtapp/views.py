from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from .models import Movie, Imdb_movie
from .forms import UserForm

now = timezone.now()

# Create your views here.

def home(request):
    return render(request, 'app/home.html')

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

def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    imovie = Imdb_movie(movie.imdb_id)
    return render(request, 'app/movie_detail.html', {
        'movie': movie,
        'imdb_movie': imovie,
    })