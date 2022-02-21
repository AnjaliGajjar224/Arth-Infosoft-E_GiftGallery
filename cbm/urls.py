from django.contrib import admin
from django.urls import include, path
from .views import HrList


urlpatterns = [
    path('list/', HrList.as_view(),name='hr_list'),
  

]