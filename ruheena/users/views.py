from django.shortcuts import redirect, render
from users.forms import UserRegisterForm, PostForm
from users.models import Post
from django.contrib.auth.decorators import login_required
# from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect

def home(request, *args, **kwargs):
    current_user = request.user
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
            # messages.success(request, 'sign up successfull')
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

            post.save()

            # messages.success(request, 'post successfully created')

    else:
        form = PostForm()
    return render(request, 'users/post.html', {'form': form})

def delete_post(request, post_id):
    print(post_id)
    post = Post.objects.get(id=post_id)
    print('deleting post', post)
    if post:
        post.delete()
        print('deleted post')
        return redirect('home')