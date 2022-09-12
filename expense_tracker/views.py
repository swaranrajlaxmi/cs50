from audioop import reverse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

from .models import User

def index(request):
    # if request.user.is_authenticated:
    #     return render(request, "")

    # else:
        # return HttpResponseRedirect(reverse("login"))
        return render(request, "login.html")


def login_view(request):
    return render(request, "login.html")


def register(request):
    return render(request, "register.html")

def logout_view(request):
    return render(request, "login.html")
