from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'orders'

urlpatterns = [
    path('create/<int:pk>/',views.order_create,name='order_create'),
    path('order_list', views.order_list, name= 'order_list'),
    path('order_detail/<int:id>/', views.order_detail, name='order_detail'),
    path('customer_order/<int:id>/', views.customer_order, name='customer_order'),
]