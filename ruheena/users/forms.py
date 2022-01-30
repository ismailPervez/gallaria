from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import EmailField

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