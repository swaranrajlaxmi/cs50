from curses import A_ALTCHARSET
from operator import truediv
from unicodedata import category
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django import forms
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from .models import User, Auction, Bid, Comment, Watchlist


class CreateListingForm(forms.ModelForm):
    class Meta:
        model = Auction
        fields = ["title", "description", "category", "image_url"]

    title = forms.CharField(label="Title", max_length=64, required=True, widget=forms.TextInput(attrs={
        "autocomplte": "off", "aria-label": "title", "class": "form-control"
    }))
    description= forms.CharField(label="Description", widget=forms.Textarea(attrs={
        "placeholder": "Describe about product", "aria-label": "description", "class": "form-control"
    }))
    image_url = forms.URLField(label="Image URL", required=False, widget=forms.URLInput(attrs={
        "class": "form-control"
    }))
    category = forms.ChoiceField(required=True, choices=Auction.CATEGORY, widget=forms.Select(attrs={
        "class": "form-control"
    }))
    current_price = forms.DecimalField(label="Price", label_suffix=False, max_digits=10, decimal_places=2, required=True, widget=forms.NumberInput(attrs={
        "type":"number", "step": "0.01", "class": "form-control"
    }))


class BidForm(forms.ModelForm):
    class Meta:
        model = Bid
        fields = ["bid_price"]
        labels = {
            "bid_price": _("")
        }
        widgets = {
            "bid_price": forms.NumberInput(attrs={
                "placeholder": "Bid",
                "min": 0.01,
                "max": 100000000,
                "class": "form-control"
            })
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["comment"]
        labels = {
            "comment": _("")
        }
        widgets = {
            "comment": forms.Textarea(attrs={
                "placeholder": "Comment",
                "class": "form-control",
                "rows": 2
            })
        }

def index(request):
    auctions = Auction.objects.filter(closed=False).order_by("publication_date")
    return render(request, "auctions/index.html", {
        "auctions": auctions
    })




@login_required
def profile(request):
    user =  Bid.objects.filter(user=request.user.id)
    bids = user.values_list("auction", flat=True).distinct()
    auctions = Auction.objects.filter(closed=True, id__in = bids).all()
    won_items = []
    for auction in auctions:
        highest_bid = Bid.objects.filter(auction=auction.id).order_by('-bid_price').first()
        
        if highest_bid.user.id == request.user.id:
            won_items.append(auction)

    selling_items = Auction.objects.filter(closed=False, seller=request.user.id).order_by("-publication_date").all()
    sold_items = Auction.objects.filter(closed=True, seller=request.user.id).order_by("-publication_date").all()
    bidding_items = Auction.objects.filter(closed=False, id__in = bids).all()

    return render(request, "auctions/profile.html", {
        "selling": selling_items,
        "sold": sold_items,
        "bidding": bidding_items,
        "won": won_items
    })






@login_required
def create_listing(request):
    if request.method == 'POST':
        create_listing_form = CreateListingForm(request.POST)
        seller = User.objects.get(pk=request.user.id)

        if create_listing_form.is_valid():
            title = create_listing_form.cleaned_data["title"]
            description = create_listing_form.cleaned_data["description"]
            category = create_listing_form.cleaned_data["category"]
            image_url = create_listing_form.cleaned_data["image_url"]
            current_price = create_listing_form.cleaned_data["current_price"]
        
            auction = Auction(
                seller = seller,
                title = title,
                description = description,
                category = category,
                image_url = image_url,
                current_price = current_price
            )
            auction.save()
            return HttpResponseRedirect(reverse("auctions:index"))

        else:
            return render(request, "auctions/create_listing.html", {
                "form": create_listing_form
            }) 

    return render(request, "auctions/create_listing.html", {
        "form": CreateListingForm()
    })



def listing_page(request, auction_id):
    
        try:
            auction = Auction.objects.get(pk=auction_id)
        except Auction.DoesNotExist:
            return render(request, "auctions/error_handling.html", {
                "status_code": 404,
                "message": "Invalid auction id"
            })
        bid = Bid.objects.filter(auction=auction_id)    
        high_bid = bid.order_by('-bid_price').first()

        if auction.closed:
            if high_bid is not None:
                winner = high_bid.user

                if request.user.id == auction.seller.id:
                    return render(request, "auctions/sold.html", {
                        "auction": auction,
                        "winner": winner
                    })
                elif request.user.id == winner.id:
                    return render(request, "auctions/bought.html", {
                        "auction": auction
                    })
            else:
                if request.user.id == auction.seller.id:
                    return render(request, "auctions/closed_without_sold.html", {
                        "auction": auction
                    })
            return HttpResponse("auction no more available")
        else:
            comments = Comment.objects.filter(auction=auction_id)
            if request.user.is_authenticated:
                watchlist_item = Watchlist.objects.filter(auction = auction_id,user = User.objects.get(id=request.user.id)).first()
                if watchlist_item is not None:
                    isOn_watchlist = True
                else:
                    isOn_watchlist = False
            else:
                isOn_watchlist = False

            if high_bid is not None:
                if high_bid.user == request.user.id:
                    bid_message = "Your bid is the highest bid"
                else:
                    bid_message = "Highest bid made by " + high_bid.user.username
            else:
                bid_message = None

            return render(request, "auctions/listing_page.html", {
                "bid_message": bid_message,
                "isOn_watchlist": isOn_watchlist,
                "comments": comments,
                "bid_form": BidForm(),
                "comment_form": CommentForm(),
                "auction": auction,
                "bid_amount": bid.count(),
            })



@login_required
def watchlist(request):
    if request.method == "POST":
        auction_id = request.POST.get("auction_id")
        try:
            auction = Auction.objects.get(pk=auction_id)
            user = User.objects.get(id=request.user.id)
        except Auction.DoesNotExist:
            return render(request, "auctions/error_handling.html", {
                "status_code": 404,
                "message": "Invalid auction id"
            })
        if request.POST.get("isOn_watchlist") == "True":
            watchlist_item = Watchlist.objects.filter(user = user,auction = auction)
            watchlist_item.delete()
        else:
            try:
                watchlist_item = Watchlist(user = user,auction = auction)
                watchlist_item.save()
            except IntegrityError:
                return render(request, "auctions/error_handling.html", {
                    "status_code": 400,
                    "message": "Already on your watchlist"
                })
        return HttpResponseRedirect("/" + auction_id)

    watchlist_auctions_ids = User.objects.get(id=request.user.id).watchlist.values_list("auction")
    watchlist_items = Auction.objects.filter(id__in=watchlist_auctions_ids, closed=False)

    return render(request, "auctions/watchlist.html", {
        "watchlist_items": watchlist_items
    })


@login_required
def bid(request):
    if request.method == "POST":
        bid_form = BidForm(request.POST)
        if bid_form.is_valid():
            bid_price = bid_form.cleaned_data["bid_price"]
            auction_id = request.POST.get("auction_id")
            auction = Auction.objects.filter(pk=auction_id).first()
            user = User.objects.filter(id=request.user.id).first()

            if auction.seller == user:
                return render(request, "auctions/error_handling.html", {
                    "status_code": 400,
                    "message": "Seller is not able to bid"
                })

            if bid_price <= 0:
                return render(request, "auctions/error_handling.html", {
                    "status_code": 400,
                    "message": "Please enter bid price greater than 0"
                })

            high_bid = Bid.objects.filter(auction=auction).order_by('-bid_price').first()
            if high_bid is None or bid_price > high_bid.bid_price:
                new_bid = Bid(auction=auction, user=user, bid_price=bid_price)
                new_bid.save()

                auction.current_price = bid_price
                auction.save()

                return HttpResponseRedirect("/" + auction_id)
            else:
                return render(request, "auctions/error_handling.html", {
                    "status_code": 400,
                    "message": "Your bid is too small for this auction"
                })
        else:
            return render(request, "auctions/error_handling.html", {
                "status_code": 400,
                "message": "Invalid Form"
            })

    return render(request, "auctions/error_handling.html", {
        "status_code": 405,
        "message": "Method Not Allowed"
    })


def categories(request, category=None):
    categories_list = Auction.CATEGORY

    if category is not None:
        if category in [choice[0] for choice in categories_list]:
            choice_in_category = [choice[1] for choice in categories_list if choice[0] == category][0]
            auctions = Auction.objects.filter(category=category, closed=False)
            
            return render(request, "auctions/category.html", {
                "auctions": auctions,
                "choice_in_category": choice_in_category
            })

    return render(request, "auctions/error_handling.html", {
        "status_code": 404,
        "message": "This page doesn't exist"
    })


@login_required
def close_auction(request, auction_id):
    try:
        auction = Auction.objects.get(pk=auction_id)
    except Auction.DoesNotExist:
        return render(request, "auctions/error_handling.html", {
            "status_code": 404,
            "message": "Auction id doesn't exist"
        })
    if request.method == "POST":
        auction.closed = True
        auction.save()
    return HttpResponseRedirect("/" + auction_id)


def comment(request, auction_id):
    if request.method == "POST":
        if request.user is not None:
            comment_form = CommentForm(request.POST)
            current_user = User.objects.get(pk=request.user.id)
            auction = Auction.objects.filter(pk=auction_id).first()
            if comment_form.is_valid():
                comment = comment_form.cleaned_data["comment"]
                comment = Comment(
                    user = current_user,
                    comment = comment,
                    auction = auction
                )
                comment.save()
            else:
                return render(request, "auctions/error_handling.html", {
                    "status_code": 400,
                    "message": "Form is invalid"
                })
        else:
            return render(request, "auctions/login.html")
            
    elif request.method == "GET":
        return render(request, "auctions/error_handling.html", {
            "status_code": 405,
            "message": "Method Not Allowed"
        })
    return HttpResponseRedirect("/" + auction_id)


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("auctions:index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("auctions:index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("auctions:index"))
    else:
        return render(request, "auctions/register.html")





def handle_not_found(request, exception):
    return render(request, "auctions/error_handling.html", {
            "status_code": 404,
            "message": "Page not found"
        })