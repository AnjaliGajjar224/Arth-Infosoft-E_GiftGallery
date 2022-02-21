from django.contrib import admin
from django.urls import include,path
from Product import views

urlpatterns =[
    
    path('addproduct/',views.addproduct),
    path('viewproduct/',views.viewproduct),
    path('productpage/',views.productpage),
    
]
