from django.urls import path
from . import views
from django.shortcuts import render
from django.http import JsonResponse

urlpatterns = [
    path('', views.main, name='main'),
    path('health/', views.health, name='health')
]