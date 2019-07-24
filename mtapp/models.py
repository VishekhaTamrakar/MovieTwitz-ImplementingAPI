from django.db import models
from django.utils import timezone
import requests

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=50)
    release_date = models.DateField(null=True)
    imdb_id = models.CharField(max_length=20)
    poster = models.CharField(max_length=500, null=True)
    genre = models.CharField(max_length=50)
    directed_by = models.CharField(max_length=50)
    runtime = models.IntegerField(blank=False)
    notable_casts = models.CharField(max_length=50)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    disc_price = models.DecimalField(max_digits=5, decimal_places=2)
    review = models.TextField()
    #audit fields
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.name)

class Imdb_movie:
    def __init__(self, imdb_id):
        url = 'https://movie-database-imdb-alternative.p.rapidapi.com/' 
        params = {
            'i': imdb_id,
            'r': 'json',
        }
        headers = {
            'X-RapidAPI-Host': "movie-database-imdb-alternative.p.rapidapi.com",
            'X-RapidAPI-Key': "fb54a2a79amshb032c359722438fp18abb9jsn80dd3fd3790f",
        }
        json_data = requests.get(url, params = params, headers = headers).json()
        print(json_data)
        self.title = json_data["Title"]
        self.year = int(json_data["Year"])
        self.imdb_rating = json_data["imdbRating"]
        self.poster = json_data["Poster"]
        print(self.title, self.year, self.imdb_rating, self.poster, sep=", ")
