from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('',views.list,name="list"),
    path('tasks/update/<str:pk>/',views.update,name="update"),
    path('tasks/delete/<str:pk>/',views.delete,name="delete"),
    
]
