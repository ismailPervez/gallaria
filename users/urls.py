from unicodedata import name
from django.urls import path
from . import views as users_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', users_views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('register/', users_views.register, name='register'),
    path('post/', users_views.post, name='post'),
    path('post/delete/<post_id>', users_views.delete_post, name='delete-post')
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)