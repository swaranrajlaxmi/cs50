from ast import If, Try
from http.client import FORBIDDEN
from urllib import response
import json
from django import http
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.core import serializers


from .models import User, Post, UserFollower


def index(request):
    return render(request, "network/index.html")

def all_posts(request):
    if(request.GET.get("following") == 'true'):
        if request.user.id is not None:
            following_to_users = UserFollower.objects.filter(follower = request.user)
            listOfFollowing = []
            for f in following_to_users:
                following = f.following.id
                listOfFollowing.append(following)
            postsQuerySet = Post.objects.filter(user__in=listOfFollowing).order_by('-timestamp')
        else: JsonResponse({}, status=403)             
    
    elif(request.GET.get("profile") != None):
        t_user = request.GET.get("profile")
        target_user = User.objects.filter(username=t_user)
        if (target_user.exists()):
            postsQuerySet = Post.objects.filter(user=target_user.first()).order_by('-timestamp')

        else: JsonResponse({}, status=404)

    else:
        postsQuerySet = Post.objects.all().order_by('-timestamp')

    paginator = Paginator(postsQuerySet, 10) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    listOfposts = []
    for p in page_obj:
        isPostOwner = False
        isLiked = False
        if request.user.id is not None:
            isLiked = p.likes.filter(id = request.user.id).exists()
            isPostOwner = (p.user.id == request.user.id)

        post = {
            'id': p.id,
            'username' : p.user.username,
            'content' : p.content, 
            'timestamp' : p.timestamp.strftime("%B %d, %Y, %I:%M %p"),  #eg - June/16/2022  11:05 PM,  
            'likes' : p.likes.count(),
            'isLiked': isLiked,
            'isPostOwner': isPostOwner
        }
        listOfposts.append(post)
    

    return JsonResponse({"posts": listOfposts, 'totalPages': paginator.num_pages })
    
@login_required
@csrf_exempt
def new_post(request):
    # Composing a new post must be via POST
    if request.method == "POST":
        data = json.loads(request.body)
        content = data.get("content")
        if len(content) != 0:
            obj = Post()
            obj.content = content
            obj.user = request.user
            obj.save()
            responseObj = {
                'id': obj.id,
                'content': obj.content,
                'username': obj.user.username,
                'timestamp': obj.timestamp.strftime("%B %d, %Y, %I:%M %p"),  #eg - June/16/2022  11:05 PM
                'likes': 0,
                'isLiked': False,
                'isPostOwner': True
            }
            print (responseObj)
            return JsonResponse(responseObj, status=201)
    return JsonResponse({}, status=404)


def profile(request, username):
    
    current_user = request.user
    target_user = User.objects.get(username=username)

    is_a_follower = UserFollower.objects.filter(follower=current_user, following=target_user).count()

    followings = UserFollower.objects.filter(follower=target_user)
    followers = UserFollower.objects.filter(following=target_user)
    
    return render(request, "network/profile.html", {
        "target_user": target_user,
        "current_user": current_user,
        "followings_count": followings.count(),
        "followers_count": followers.count(),
        "is_a_follower": is_a_follower
    })

@login_required
@csrf_exempt
def following(request):
    return render(request, "network/following.html")



@login_required
@csrf_exempt
def follow(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get("username")

        current_user = request.user
        target_user = User.objects.get(username=username)

        follower_queryset = UserFollower.objects.filter(follower=current_user, following=target_user)
        is_a_follower = follower_queryset.count()

        # Unfollow
        if(is_a_follower != 0):
            follower_queryset.delete()
        else:
        # Folllow user
            user_follower = UserFollower()
            user_follower.follower = request.user
            user_follower.following = target_user
            user_follower.save()

        followers = UserFollower.objects.filter(following=target_user) 
            
        return JsonResponse({
            "followers_count": followers.count(),
        }, status=201) 


@login_required
@csrf_exempt
def like(request):
    if request.method == "POST":
        data = json.loads(request.body)
        post_id = data.get("postId")
        try:
            post = Post.objects.get(id = post_id)
        except Exception:
            return JsonResponse({
                "message": "post not found."
            }, status=404)

        current_like_status = post.likes.filter(id = request.user.id).exists()   
        #dislike
        if current_like_status == True:
            post.likes.remove(request.user)
        #like
        else:
            post.likes.add(request.user)
        
        likes = post.likes.count()

        return JsonResponse( {
            "current_like_status": not current_like_status,
            "likes": likes
            }, status=201)


@login_required
@csrf_exempt
def save_edited_post(request):
    if request.method == "POST":
        data = json.loads(request.body)
        content = data.get("content")
        post_id = data.get("postId")

        try:
            post = Post.objects.get(id = post_id)
        except Exception:
            return JsonResponse({
                "message": "post not found."
            }, status=404)

        if request.user.id is not None:
            isPostOwner = (post.user.id == request.user.id)

            if len(content) != 0 and isPostOwner == True:
                post.content = content
                post.save()
                return JsonResponse({
                    'timestamp': post.timestamp.strftime("%B %d, %Y, %I:%M %p"),  #eg - June/16/2022  11:05 PM
                },status=200)
            else:
                return JsonResponse({"message": "Insufficient post length"},status=400)#400 - bad request 
    


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
