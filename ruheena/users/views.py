from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("home page")

def login(request):
    return HttpResponse("login page")

def register(request):
    return HttpResponse("register page")