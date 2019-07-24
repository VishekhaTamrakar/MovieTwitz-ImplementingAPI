from django.contrib import admin
from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'app'

urlpatterns = [
    path('', views.home, name='home'),
    url(r'^home/$', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('movie/<int:pk>/detail', views.movie_detail, name='movie_detail'),
]