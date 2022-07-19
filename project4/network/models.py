from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='poster')
    content = models.CharField(max_length=500, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now=True)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.likes

class Profile(models.Model):
    follower = models.ForeignKey(User, related_name='from_user', on_delete=models.CASCADE)
    following = models.ForeignKey(User, related_name='to_user', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.follower} follows {self.following}'


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='liked_user')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='liked_post')
    
    def __str__(self):
        return str(self.post)