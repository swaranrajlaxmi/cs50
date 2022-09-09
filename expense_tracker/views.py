from django.shortcuts import render
from django.http import HttpResponse

import expense_tracker

def index(request):
    return HttpResponse("hello django!")


def login_view(request):
    return render(request, "expense_tracker/login.html")
