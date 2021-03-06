from django.contrib import admin
from django.conf.urls import url
from django.contrib.auth import views as auth_views

from rest_framework_jwt.views import obtain_jwt_token

from . import views
from django.urls import path

app_name = 'app'

urlpatterns = [
    path('', views.home, name='home'),
    url(r'^home/$', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('About/', views.About, name='About'),
    path('Contact/', views.Contact, name='Contact'),
  
    path('movie_list', views.movie_list, name='movie_list'),
    path('movie/<int:pk>/edit/', views.movie_edit, name='movie_edit'),
    path('movie/<int:pk>/delete/', views.movie_delete, name='movie_delete'),
    path('movie/create/', views.movie_new, name='movie_new'),

    path('movie/<int:pk>/detail', views.movie_detail, name='movie_detail'),
    path('movie/<str:pk>/detail', views.imdb_movie_detail, name='imdb_movie_detail'),
    path('movie_search', views.movie_search, name='movie_search'),
    path('movie_nearby', views.movie_nearby, name='movie_nearby'),

    url(r'^$', views.product_list, name='product_list'),
    path('product', views.product_list, name='product_list'),
    path('product/<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('product/<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),

    url(r'^api/movies/$', views.movie_list_rest),
    path('api/movies/<str:pk>', views.get_movie_rest),
]
