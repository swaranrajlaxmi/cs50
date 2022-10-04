import json
from django.urls import reverse
from sqlite3 import IntegrityError
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from .models import User, Settings, CURRENCY_CHOICES

def index(request):
    if request.user.is_authenticated:
        return render(request, "expense.html")

    else:
        return HttpResponseRedirect(reverse("login"))


def profile(request):
    return render(request, "profile.html")


def budget(request):
    return render(request, "budget.html")


def create_budget(request):
    return render(request, "create_budget.html")


def add_expense(request):
    return render(request, "add_expense.html")


@login_required
@csrf_exempt
def settings(request):
    if request.method == "POST":
        data = json.loads(request.body)
        currency = data.get("currency")
        reset_day = data.get("day")
        user = request.user

        if currency and reset_day is not None:
            settings = Settings.objects.update(user=user, currency=currency, reset_day=reset_day)
            
        return JsonResponse({}, status=201)
    else:
        currency_choices = CURRENCY_CHOICES
        list_of_currency_choices = []
        for first, _ in currency_choices:
            list_of_currency_choices.append(first)
        days = []
        for day in range(1, 29):
            days.append(day)

        user = request.user
        #bydefault users currency and reset_day
        currency = Settings.objects.filter(user=user).first().currency
        reset_day = Settings.objects.filter(user=user).first().reset_day
        return render(request, "settings.html", {
            "list_of_currency_choices": list_of_currency_choices,
            "selected_currency": currency,
            "days": days,
            "selected_day": reset_day
        })


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
            user.save()
            settings = Settings.objects.create(user=user)
            settings.save()

        except IntegrityError:
            return render(request, "register.html", {
                "message": "Username already taken."
            })

        login(request, user)
        return HttpResponseRedirect(reverse("create_budget"))
    else:
        return render(request, "register.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))



