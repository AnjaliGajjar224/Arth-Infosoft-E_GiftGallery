from django.contrib import admin
from django.urls import include, path
from .views import CreateTicket, DeleteTicket, TaskDetail, UpdateTicket
from ticket import views

urlpatterns = [
   
   path('add/',CreateTicket.as_view()),
   path('view/',views.index),
   path('<pk>/delete/',DeleteTicket.as_view()),
   path('<pk>/update/',UpdateTicket.as_view()),
   path('<pk>/view/',TaskDetail.as_view()),

]