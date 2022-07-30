from django.contrib import admin
from .models import User, Post, UserFollower

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    """Contains User model admin page config"""
    list_display = ("id", "username", "email", "password")
    

class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "timestamp" )

class UserFollowerAdmin(admin.ModelAdmin):
    list_display = ("id", "follower", "following" )

admin.site.register(User, UserAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(UserFollower, UserFollowerAdmin)