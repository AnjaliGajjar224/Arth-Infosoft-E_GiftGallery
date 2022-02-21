from django.contrib import admin
from django.urls import include, path
from orm import views

urlpatterns = [
    
    path('productdata/', views.productdata),
    


]