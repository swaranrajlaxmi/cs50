from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("profile", views.profile, name="profile"),
    path("budget", views.budget, name="budget"),
    path("create_budget", views.create_budget, name="create_budget"),
    path("add_expense", views.add_expense, name="add_expense"),
    path("settings", views.settings, name="settings"),
]