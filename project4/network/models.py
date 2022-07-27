from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    follower = models.ManyToManyField('self', blank=True, related_name='follower')


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='poster')
    content = models.CharField(max_length=500, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, blank=True, related_name='like')
