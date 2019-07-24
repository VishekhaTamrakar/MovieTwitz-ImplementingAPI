from django import forms
from django.contrib.auth.models import User
from .models import Movie

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('name', 'release_date', 'imdb_id', 'genre', 'poster', 'directed_by', 'runtime', 'notable_casts', 'rating', 'disc_price', 'review')