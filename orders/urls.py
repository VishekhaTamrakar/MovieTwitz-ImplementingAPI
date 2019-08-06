from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'orders'

urlpatterns = [
    url(r'^create/$',views.order_create,name='order_create'),
    path('order_list', views.order_list, name='order_list'),
    path('admin/order/<int:order_id>/', views.admin_order_detail, name='admin_order_detail'),
    ]