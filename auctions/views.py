from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Listings,User,Bids,Comment,All


def index(request):
    all=All.objects.all()
    return render(request,"auctions/index.html",{
        "items":all
    })


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
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


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
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def create(request):
    try:
        return render(request,"auctions/create.html")
    except:
        return render(request,"auctions/create.html")

def submit(request):
    if request.method=="POST":
        list=Listings()
        all=All()
        list.owner=request.user.username
        list.title=request.POST.get('title')
        list.desc=request.POST.get('desc')
        list.price=request.POST.get('price')
        list.email=request.POST.get('email')
        list.category=request.POST.get('category')
        list.link=request.POST.get('link')
        list.save()

        items=list.objects.all()
        for i in items:
            all.listing_id=i.id
            all.title=i.title
            all.desc=i.desc
            all.link=i.link
