from django.contrib import admin
from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'portfolio'

urlpatterns = [
    path('', views.home, name='home'),
    url(r'^home/$', views.home, name='home'),
]