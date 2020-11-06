from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'docs/landingpage.html')

def navbar(request):
    return render(request, 'docs/navbar.html')

def profile(request):
    return render(request, 'docs/profile.html')

def detail(request):
    return render(request, 'docs/detail.html')

def search(request):
    return render(request, 'docs/searchPage.html')

def login(request):
    return render(request, 'docs/login.html')

def delete(request):
    return render(request, 'docs/delete.html')
