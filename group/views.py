from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def group(request):
    return HttpResponse("Group called......")

def index(request):
    context={
        'name':'E-Gift Gallery',
    }
    return render(request,'group/index.html',context)

def contactUs(request):
    context={
        'contact_name':['Anjali','Bittu','Krishiv','Dwij','Yashvi']
    }
    return render(request,'group/contactUs.html',context)

def AboutUs(request):
    context={
        'isActive':True,
        'age': 20 ,
    }
    return render(request,'group/AboutUs.html',context)
