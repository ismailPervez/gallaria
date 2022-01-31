from pyexpat import model
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Post(models.Model):
    CATEGORY_CHOICES = (
        ('memory', 'memory'),
        ('travel', 'travel'),
        ('vacation', 'vacation'),
        ('home', 'home')
    )
    picture = CloudinaryField('image')
    caption = models.CharField(max_length=220)
    date_posted = models.DateField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=8, choices=CATEGORY_CHOICES, default='memory')