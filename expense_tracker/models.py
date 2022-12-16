from email.policy import default
from sre_constants import CATEGORY
from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser
from babel.numbers import list_currencies

CATEGORY_CHOICES = [
        ('FD', 'Food & Drinks'),
        ('SG', 'Shopping'),
        ('RT', 'Rent'),
        ('TL', 'Travel'),
        ('SS', 'Sports'),
        ('IT', 'Internet'),
        ('IS', 'Investments'),
        ('ET', 'Entertainment'),
        ('SY', 'Study'),
        ('VE', 'Vehicle'),
        ('TN', 'Transportation'),
        ('GS', 'Groceries'),
        ('KS', 'Kids'),
        ('GT', 'Gifts'),
        ('GL', 'General'),
        ('FL', 'Fuel'),
        ('HS', 'Holidays'),
    ] 
# Create your models here.
class User(AbstractUser):
    pass


CURRENCY_CHOICES = [(currency, currency) for currency in list_currencies()] 

class Settings(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    currency = models.CharField(max_length=3, default='USD', choices=CURRENCY_CHOICES)
    reset_day = models.IntegerField(default=1)


class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    budget_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)


class Category(models.Model):
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES)


class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category =  models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    date = models.DateTimeField()
    notes = models.CharField(max_length=500, null=True, blank=True)