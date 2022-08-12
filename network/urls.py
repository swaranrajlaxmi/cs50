
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("profile/<str:username>", views.profile, name="profile"),

    #API Routes
    path("create_post", views.new_post),
    path("posts", views.all_posts, name="posts"),
    path("follow", views.follow),
    path("like", views.like),
    path("save_edited_post", views.save_edited_post),
    path("following", views.following, name="following"),
]
