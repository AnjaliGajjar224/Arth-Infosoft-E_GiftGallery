from gc import DEBUG_COLLECTABLE
from itertools import product
from sre_constants import CATEGORY
from telnetlib import STATUS
from unicodedata import category
from django.db import models

# Create your models here.
class Role(models.Model):
    role_name = models.CharField(max_length=50)
    role_description = models.TextField()
    
    class Meta:
        db_table = 'role'
    
class Buyer(Role):

    buyer_name=models.CharField(max_length=50)
    buyer_email=models.CharField(max_length=50)
    buyer_password=models.CharField(max_length=50)
    buyer_phone=models.CharField(max_length=50)
    buyer_address=models.TextField()
    buyer_dob=models.DateField()

    class Meta:
         db_table='buyer'



"""
    For relationship 
    Query :
        role_id=models.ForeignKey(Role, on_delete=modelIs,CASCADE)
        role_id=models.OneToOneField(Role, on_delete=models.CASCADE)

"""
class Customer(models.Model):
    customer_name = models.CharField(max_length=200)

    class Meta:
        db_table = 'customer'

class Product(models.Model):
    CATEGORY=(('indoor','indoor'),('outdoor','outdoor'))
    name = models.CharField(max_length=200)
    price= models.FloatField()
    date_created= models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'product'

class Order(models.Model):
    STATUS = (('pending','pending'),('od','od'),('delivered','delivered'))
    customer = models.ForeignKey(Customer, null= True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null= True, on_delete=models.SET_NULL)
    date_created= models.DateTimeField(auto_now_add=True)
    status= models.CharField(max_length=200,choices=STATUS)
    class Meta:
        db_table = 'order'

"""
 In One Department Many Employees are working with different many responsibility
"""