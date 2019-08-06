from django.db import models
from django.utils import timezone
import requests
from django.urls import reverse

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
        #print(json_data)
        self.title = json_data["Title"]
        self.year = int(json_data["Year"])
        self.imdb_rating = json_data["imdbRating"]
        self.poster = json_data["Poster"]
        print(self.title, self.year, self.imdb_rating, self.poster, sep=", ")

class Box_Office(models.Model):
    imdb_id = models.CharField(max_length=10)
    movie_name = models.CharField(max_length=50)
    poster = models.CharField(max_length=500, null=True)
    refreshed_date = models.DateField()
    #updated_date = models.DateTimeField(auto_now_add=True)

class Category(models.Model):
    name = models.CharField(max_length=200,
                            db_index=True)
    slug = models.SlugField(max_length=200,
                            unique=True)

    class Meta:
            ordering = ('name',)
            verbose_name = 'category'
            verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.CharField(max_length=500, null=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('app:product_detail',
                       args=[self.id, self.slug])

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name