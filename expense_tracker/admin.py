from django.contrib import admin
from .models import User, Settings, Budget, Expense, Category


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    """Contains User model admin page config"""
    list_display = ("id", "username", "email", "password")


class SettingsAdmin(admin.ModelAdmin):
    list_display = ("id", "currency", "reset_day" )


class BudgetAdmin(admin.ModelAdmin):
    list_display = ("id", "budget_amount" )


class ExpenseAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "amount", "notes", "date", "category" )


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "category" )

admin.site.register(User, UserAdmin)
admin.site.register(Settings, SettingsAdmin)
admin.site.register(Budget, BudgetAdmin)
admin.site.register(Expense, ExpenseAdmin)
admin.site.register(Category, CategoryAdmin)