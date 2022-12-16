from distutils.log import error
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
from django.db.models import Sum
from django.contrib.auth.hashers import check_password
import calendar

from .models import User, Settings, Budget, CURRENCY_CHOICES, Category, CATEGORY_CHOICES, Expense

def index(request):
    if request.user.is_authenticated:
        budget_dates = get_expense_budget_period(request.user)
        expenses = Expense.objects.filter(user = request.user, date__gte=budget_dates["start_date"], date__lte=budget_dates["end_date"]).order_by('-date')
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
            "expenses": expenses_list,
            "length": len(expenses_list)
        })

    else:
        return HttpResponseRedirect(reverse("login"))


def get_expense_budget_period(user):
    settings = Settings.objects.filter(user=user).first()
    today = date.today()
    year = today.year
    month = today.month
    reset_date = date(year, month, settings.reset_day)
    if today < reset_date:
        start_date = reset_date - timedelta(mdays[reset_date.month]) + timedelta(days=1)
        end_date = reset_date - timedelta(days=1)
    else:
        start_date = reset_date 
        end_date = start_date + timedelta(mdays[reset_date.month]) - timedelta(days=1)

    return {
        "start_date": start_date,
        "end_date": end_date,
    }

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
        data = json.loads(request.body)
        old_password = data.get("oldPassword")
        new_password = data.get("newPassword")
        confirm_password = data.get("confirmPassword")

        if new_password != confirm_password:
            return JsonResponse({
                "message": "Password and Confirm Password should be same."
            }, status=401)

        user = User.objects.get(username__exact=request.user)
        if check_password(old_password, user.password):
            user.set_password(new_password)
            user.save()

            login(request, user)

            return JsonResponse({
                "message": "Password changed successfully."
            })
    else:
        return render(request, "profile.html")
    



@login_required
@csrf_exempt
def budget(request):
    user = request.user
    budget = Budget.objects.filter(user=user).last()
    settings = Settings.objects.filter(user=user).first()
    
    budget_dates = get_expense_budget_period(request.user)
    formatted_end_date = budget_dates['end_date'].strftime("%d-%b-%Y")
    formatted_start_date = budget_dates['start_date'].strftime("%d-%b-%Y")

    expense_count = Expense.objects.filter(user=user).count()
    if expense_count != 0:
        total_expense_amount = Expense.objects.filter(user=user).aggregate(Sum('amount'))['amount__sum']
        
    else:
        total_expense_amount = 0

    if budget is not None:
        return render(request, "budget.html",{
            "budget_amount": budget.budget_amount,
            "currency": settings.currency,
            "start_date": formatted_start_date,
            "end_date": formatted_end_date,
            "left_amount": (budget.budget_amount-total_expense_amount)
        })
    else:
        return HttpResponseRedirect(reverse("set_budget"))


@login_required
@csrf_exempt
def set_budget(request):
    if request.method == "POST":
        budget_amount = request.POST["budget-amount"]
        budget = Budget.objects.filter(user=request.user).update(budget_amount=budget_amount )
        
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
                "start_date": start_date.strftime("%d-%b-%Y"),
                "budget_amount": budget.budget_amount
                })

        else:
            return render(request, "set_budget.html", {
                "currency": currency, 
                "start_date": start_date.strftime("%d-%b-%Y"),
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
        try:
            id = form.get("id") 
        except Exception:
            return JsonResponse({
                "message": "id not found."
            }, status=404)

        if id is not '':
            Expense.objects.filter(id=id).update(user=request.user, category=category, amount=amount, date=date, notes=notes)
            return HttpResponseRedirect(reverse("index"))
        else:
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
        form = request.POST
        currency = form.get("currency_choices")
        reset_day = form.get("days")
        user = request.user

        if currency and reset_day is not None:
            settings = Settings.objects.filter(user=user).update(currency=currency, reset_day=reset_day)
            
        return HttpResponseRedirect(reverse("budget"))
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

        except:
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



