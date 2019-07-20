from django.contrib import admin
from .models import Movie

# Register your models here.
class MovieList(admin.ModelAdmin):
    list_display = ('name', 'directed_by')
    list_filter = ('rating', 'genre')
    search_fields = ('name', 'imdb_id')
    ordering = ['name']

admin.site.register(Movie, MovieList)