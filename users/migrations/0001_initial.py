# Generated by Django 4.0.1 on 2022-02-01 10:35

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('caption', models.CharField(max_length=220)),
                ('date_posted', models.DateField(default=django.utils.timezone.now)),
                ('category', models.CharField(choices=[('memory', 'memory'), ('travel', 'travel'), ('vacation', 'vacation'), ('home', 'home')], default='memory', max_length=8)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
