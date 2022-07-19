from urllib import response
import json
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


from .models import User, Post, Profile, Like


from .models import User


def index(request):
    posts = Post.objects.all().order_by('-timestamp')

    paginator = Paginator(posts, 10) # Show 10 posts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "network/index.html", {'page_obj': page_obj})

@login_required
@csrf_exempt
def new_post(request):
    # Composing a new post must be via POST
    if request.method == "POST":
        data = json.loads(request.body)
        post = data.get("content")
        if len(post) != 0:
            obj = Post()
            obj.content = post
            obj.user = request.user
            obj.save()
            responseObj = {
                'post_id': obj.id,
                'username': obj.user.username,
                'timestamp': obj.timestamp.strftime("%B %d, %Y, %I:%M %p")  #eg - June/16/2022  11:05 PM
            }
            print (responseObj)
            return JsonResponse(responseObj, status=201)
    return JsonResponse({}, status=400)




def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")
