from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from .models import Movie

now = timezone.now()

# Create your views here.

def home(request):
    return render(request, 'app/home.html')