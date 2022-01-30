from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    picture = models.ImageField(upload_to='gallery/')
    caption = models.CharField(max_length=220)
    date_posted = models.DateField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)