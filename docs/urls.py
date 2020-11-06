from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('navbar/', views.navbar),
    path('profile/', views.profile),
    path('detail/', views.detail),
    path('search/', views.search),
    path('login/', views.login),
    path('delete/', views.delete),
    
]
