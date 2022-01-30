from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def home(request):
    return render(request, 'users/index.html')

def login(request):
    return render(request, 'users/login.html', {'title': 'login to your personal gallery - Ruheena'})

def register(request):
    form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})