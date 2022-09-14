from django.urls import reverse
from sqlite3 import IntegrityError
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth import authenticate, login, logout

from .models import User

def index(request):
    if request.user.is_authenticated:
        return render(request, "expense.html")

    else:
        return HttpResponseRedirect(reverse("login"))


def login_view(request):
    if request.method == "POST":

        username = request.POST["username"] 
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
    
        else:
            return render(request, "login.html", {
                "message": "Invalid username and/or password."
            })
    return render(request, "login.html")


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]

        if password != confirmation:
            return render(request, "register.html",{
                "message": "Password and Confirm Password should be same."
            })

        try:
            user = User.objects.create_user(username, email, password)
            # user = User()
            # user.username = username
            # user.email = email
            # user.password = password
            user.save()
        except IntegrityError:
            return render(request, "register.html", {
                "message": "Username already taken."
            })

        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "register.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))
