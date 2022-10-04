from django.contrib import admin
from .models import User, Settings


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    """Contains User model admin page config"""
    list_display = ("id", "username", "email", "password")


class SettingsAdmin(admin.ModelAdmin):
    list_display = ("id", "currency", "reset_day" )


admin.site.register(User, UserAdmin)
admin.site.register(Settings, SettingsAdmin)