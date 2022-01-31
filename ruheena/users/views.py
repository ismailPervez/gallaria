from django.shortcuts import render
from users.forms import UserRegisterForm, PostForm
from users.models import Post
from django.utils.functional import SimpleLazyObject
from django.contrib.auth.decorators import login_required

def home(request):
    current_user = request.user
    # print(isinstance(current_user, SimpleLazyObject))
    if current_user.is_authenticated:
        posts = Post.objects.filter(user=current_user)
    else:
        posts = None
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

@login_required
def post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = Post(
                picture=form.cleaned_data['picture'],
                caption=form.cleaned_data['caption'],
                user=request.user
            )

            # print(post.date_posted)
            # print(post.picture.url)
            post.save()

    else:
        form = PostForm()
    return render(request, 'users/post.html', {'form': form})