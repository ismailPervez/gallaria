from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import EmailField, ModelForm
from users.models import Post

class UserRegisterForm(UserCreationForm):
    email =  EmailField(required=True)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = [
            'picture',
            'caption'
        ]