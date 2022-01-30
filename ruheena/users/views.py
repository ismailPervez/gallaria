from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'users/index.html')

def login(request):
    return render(request, 'users/login.html')

def register(request):
    return HttpResponse("register page")