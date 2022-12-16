from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("profile", views.profile, name="profile"),
    path("budget", views.budget, name="budget"),
    path("set_budget", views.set_budget, name="set_budget"),
    path("add_expense", views.add_expense, name="add_expense"),
    path("settings", views.settings, name="settings"),
    path("change_password", views.change_password, name="change_password"),
    path("expense_category", views.get_category_agg, name="expense_category"),
    
]