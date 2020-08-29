from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listings(models.Model):
    owner=models.CharField(max_length=64)
    title=models.CharField(max_length=64)
    desc=models.TextField()
    price=models.IntegerField()
    email=models.EmailField(max_length=254)
    category=models.CharField(max_length=64)
    datetime=models.DateTimeField(auto_now_add=True)
    link = models.CharField(max_length=64,default=None,blank=True,null=True)

class Bids(models.Model):
    uname=models.CharField(max_length=64)
    title=models.IntegerField()
    highest_bid=models.IntegerField()
    first_bid=models.IntegerField()
    listing_id=models.IntegerField()

class Comment(models.Model):
    uname=models.CharField(max_length=64)
    cmt=models.TextField()
    datetime=models.DateTimeField(auto_now_add=True)

class All(models.Model):
    listing_id=models.IntegerField()
    title=models.CharField(max_length=64)
    desc=models.TextField()
    link = models.CharField(max_length=64,default=None,blank=True,null=True)
