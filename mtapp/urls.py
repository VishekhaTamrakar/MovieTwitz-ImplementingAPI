from django.contrib import admin
from django.conf.urls import url
from django.contrib.auth import views as auth_views


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
]
