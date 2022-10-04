from django.db import models
from django.contrib.auth.models import AbstractUser
from babel.numbers import list_currencies

# Create your models here.
class User(AbstractUser):
    pass


CURRENCY_CHOICES = [(currency, currency) for currency in list_currencies()] 

class Settings(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    currency = models.CharField(max_length=3, default='USD', choices=CURRENCY_CHOICES)
    reset_day = models.IntegerField(default=1)