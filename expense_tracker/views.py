import json
from django.urls import reverse
from sqlite3 import IntegrityError
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from datetime import date, datetime, timedelta
from calendar import mdays
import calendar

from .models import User, Settings, Budget, CURRENCY_CHOICES, Category, CATEGORY_CHOICES, Expense

def index(request):

    if request.user.is_authenticated:
        expenses = Expense.objects.filter(user = request.user).order_by('-date')
        expenses_list = []
        for expense in expenses:
            expense = {
                'id': expense.id,
                'date': expense.date.strftime("%a, %-d %B %Y"),
                'amount': expense.amount,
                'category': expense.category.get_category_display(),
                'notes': expense.notes,
                
            }
            expenses_list.append(expense)
            

        return render(request, "index.html", {
            "expenses": expenses_list
        })

    else:
        return HttpResponseRedirect(reverse("login"))


@login_required
@csrf_exempt
def profile(request):
    if request.method == "POST":
        return render(request, "profile.html")
    else:
        user = User.objects.filter(username = request.user).first()
        return render(request, "profile.html", {
            "username": user.username,
            "email": user.email 
        })


@login_required
@csrf_exempt
def change_password(request):
    if request.method == "POST":

        return render(request, "profile.html")
    else:
        return render(request, "profile.html")
    



@login_required
@csrf_exempt
def budget(request):
    user = request.user
    budget = Budget.objects.filter(user=user).last()
    settings = Settings.objects.filter(user=user).first()
    # day = settings.reset_day
    today = date.today()
    year = today.year
    month = today.month
    start_date = datetime(year, month, settings.reset_day)
    next_start_date = start_date + timedelta(mdays[start_date.month])
    end_date = next_start_date - timedelta(days=1)
    formatted_end_date = end_date.strftime("%d-%m-%Y")
    
    
    formatted_start_date = start_date.strftime("%d-%m-%Y")

    if budget is not None:
        return render(request, "budget.html",{
            "budget_amount": budget.budget_amount,
            "currency": settings.currency,
            "start_date": formatted_start_date,
            "end_date": formatted_end_date
        })
    else:
        return HttpResponseRedirect(reverse("set_budget"))


@login_required
@csrf_exempt
def set_budget(request):
    if request.method == "POST":
        budget_amount = request.POST["budget-amount"]
        budget = Budget.objects.update(user=request.user, budget_amount=budget_amount )
        
        return HttpResponseRedirect(reverse("budget"))
    else:
        settings = Settings.objects.filter(user=request.user).first()
        budget = Budget.objects.filter(user=request.user).last()
        day = settings.reset_day
        currency = settings.currency
        today = date.today()
        year = today.year
        month = today.month
        start_date = datetime(year, month, day)

        if budget.budget_amount != 0:

            return render(request, "set_budget.html", {
                "currency": currency, 
                "start_date": start_date.strftime("%d-%m-%Y"),
                "budget_amount": budget.budget_amount
                })

        else:
            return render(request, "set_budget.html", {
                "currency": currency, 
                "start_date": start_date.strftime("%d-%m-%Y"),
                "budget_amount": 0
                })


@login_required
@csrf_exempt
def add_expense(request):
    if request.method == "POST":
        form = request.POST
        amount = form.get("expense_amount")
        category_key = form.get("category_key")
        date = form.get("expense_date")
        notes = form.get("expense_notes")

        category = Category.objects.filter(category = category_key ).first()

        if len(form) != 0:
            obj = Expense()
            obj.user = request.user
            obj.category = category
            obj.date = date
            obj.notes = notes
            obj.amount = amount
            obj.save()

        return HttpResponseRedirect(reverse("index"))
    else:
        id = request.GET.get('id')
        
        if id is not None:
            expense = Expense.objects.filter(id = id).first()

            return render(request, "add_expense.html", {
            "category_choices": CATEGORY_CHOICES,
            'date': expense.date.strftime("%Y-%m-%d"),
            'amount': expense.amount,
            'category': expense.category.get_category_display(),
            'notes': expense.notes,
            'id': id
        })
        else:
           return render(request, "add_expense.html", {
            "category_choices": CATEGORY_CHOICES
        })


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
            budget = Budget.objects.create(user=user)
            budget.save()

        except IntegrityError:
            return render(request, "register.html", {
                "message": "Username already taken."
            })

        login(request, user)
        return HttpResponseRedirect(reverse("set_budget"))
    else:
        return render(request, "register.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))



