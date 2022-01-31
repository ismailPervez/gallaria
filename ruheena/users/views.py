from django.shortcuts import render
from users.forms import UserRegisterForm
from users.models import Post
from django.utils.functional import SimpleLazyObject

def home(request):
    current_user = request.user
    if not isinstance(current_user, SimpleLazyObject):
        posts = None
    else:
        posts = Post.objects.filter(user=current_user)
    return render(request, 'users/index.html', {'posts': posts})

def login(request):
    return render(request, 'users/login.html', {'title': 'login to your personal gallery - Ruheena'})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})