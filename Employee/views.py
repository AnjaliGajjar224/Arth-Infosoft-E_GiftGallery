from django.http import HttpResponse
from django.shortcuts import render

from .models import Employee

# Create your views here.
def addEmployee(request):
    emp = Employee(ename='John',eage=25,eemail='Jhon@gmail.com',econtact=987654321)
    
    emp.save()

    return HttpResponse("Employee added...")

def viewEmployee(request):
    employees = Employee.objects.all().values_list()
    print(employees)
    return render(request,'employee/view.html',{'employees':employees})

def deleteEmployee(request):
    emp = Employee.objects.get(id=4)
    emp.delete()
    return HttpResponse("Employee Deleted....")

def updateEmployee(request):
    emp = Employee.objects.get(id=1)
    emp.eage = 30
    emp.econtact=9865322741
    emp.save()
    return HttpResponse("Employee Updated...")

