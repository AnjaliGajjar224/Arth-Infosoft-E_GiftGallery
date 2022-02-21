from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def addproduct(request): 
    return HttpResponse("Add product called....")

def viewproduct(request): 
    return HttpResponse("View product called....")

def productpage(request):
    return render(request,'product/productpage.html')

