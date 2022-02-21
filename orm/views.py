from multiprocessing import context
from webbrowser import get
from django.shortcuts import render

from .models import Product

# Create your views here.

def productdata(request):
        
        products = Product.objects.all().values()
      #  p1=Product.objects.filter(namestartswith())
        
        product_list=[]
        for i in products:
            product_list.append(i)
        
        print("Product_list..",product_list)
       
        """for product in products:
            print(product.keys(),ends=" ")
            print(product.values())"""
        context = {
            'products':product_list

        }
       
        return render(request,'orm/product.html',context)