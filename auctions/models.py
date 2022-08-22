from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """User model - inherits from AbstractUser (Django implementation)"""
    pass

class Auction(models.Model):
    AUDIO = 'AO'
    BOOKS = 'BK'
    MENS_FASHION = 'MF'
    WOMENS_FASHION = 'WF'
    FOODS_DRINKS = 'FD'
    ELECTRONICS = 'EL'
    SPORTS = 'SP'
    HOME_DECOR = 'HD'
    COLLECTIBLES_ARTS = 'CA'
    TOYS = 'TY'

    CATEGORY = [
        (AUDIO, "Audio"),
        (BOOKS, "Books"),
        (MENS_FASHION, "Men's Fashion"),
        (WOMENS_FASHION, "Women's Fashion"),
        (FOODS_DRINKS, "Foods & Drinks"),
        (ELECTRONICS, "Electronics"),
        (SPORTS, "Sports"),
        (HOME_DECOR, "Home Decor"),
        (COLLECTIBLES_ARTS, "Collectibles & Art"),
        (TOYS, "Toys"),
    ]

    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=64, blank=False)
    description = models.CharField(max_length=300, blank=True)
    current_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    category = models.CharField(max_length=3, choices=CATEGORY, default=AUDIO)
    image_url = models.URLField(blank=True)
    publication_date = models.DateTimeField(auto_now_add=True)
    closed = models.BooleanField(default=False)

    class Meta:
        verbose_name = "auction"
        verbose_name_plural = "auctions"

    def __str__(self):
        return f"Auction id: {self.id}, title: {self.title}, seller: {self.seller}"


class Bid(models.Model):
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bid_date = models.DateTimeField(auto_now_add=True)
    bid_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "bid"
        verbose_name_plural = "bids"

    def __str__(self):
        return f"{self.user} bid {self.bid_price} on {self.auction}"


class Comment(models.Model):
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(blank=False)
    comment_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "comment"
        verbose_name_plural = "comments"

    def __str__(self):
        return f"{self.id} comment on auction {self.auction} made by {self.user}"



class Watchlist(models.Model):
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="watchlist")

    class Meta:
        verbose_name = "watchlist"
        verbose_name_plural = "watchlists"
        # Forces to not have auction duplicates for one user
        unique_together = ["auction", "user"]

    def __str__(self):
        return f"{self.auction} on user {self.user} watchlist"