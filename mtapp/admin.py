from django.contrib import admin
from .models import Movie, Box_Office,Category, Product

# Register your models here.
class MovieList(admin.ModelAdmin):
    list_display = ('name', 'directed_by')
    list_filter = ('rating', 'genre')
    search_fields = ('name', 'imdb_id')
    ordering = ['name']

class BoxOfficeList(admin.ModelAdmin):
    list_display = ('pk', 'imdb_id', 'movie_name')
    search_fields = ('movie_name', 'imdb_id')
    ordering = ['pk']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug']
	prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug', 'price', 'available', 'created', 'updated']
	list_filter = ['available', 'created', 'updated']
	list_editable = ['price', 'available']
	prepopulated_fields = {'slug': ('name',)}

admin.site.register(Movie, MovieList)
admin.site.register(Box_Office, BoxOfficeList)