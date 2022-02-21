from django.contrib import admin
from django.urls import include, path
from group import views

urlpatterns = [
    path('add/', views.group),
    path('contactUs/', views.contactUs),
    path('index/', views.index),
    path('aboutus/', views.AboutUs),


]