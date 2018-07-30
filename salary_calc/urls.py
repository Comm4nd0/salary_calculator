from django.contrib import admin
from django.urls import path
from calculator import views

urlpatterns = [
    path('admin', admin.site.urls, name='admin'),
    path('', views.calc, name='calc'),
    path('net', views.net_calc, name='net'),
]
