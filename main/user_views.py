from django.shortcuts import render, redirect
from django.http import HttpResponse

#
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.forms import UserCreationForm

#


def loginPage(req):
    if req.user.is_authenticated:
        return redirect("home")
    if req.method == "POST":
        username = req.POST.get("username").lower()
        password = req.POST.get("password")

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(req, "User does not exist")

        user = authenticate(req, username=username, password=password)

        if user is not None:
            login(req, user)
            return redirect("home")
        else:
            messages.error(req, "Username and password does not match")

    context = {}
    return render(req, "main/login.html", context)


def logoutPage(req):
    logout(req)
    context = {}
    return redirect("home")


def registerPage(req):
    if req.user.is_authenticated:
        return redirect("home")
    form = UserCreationForm()
    if req.method == "POST":
        try:
            form = UserCreationForm(req.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.username = user.username.lower()
                user.save()
                login(req, user)
                return redirect("home")
            else:
                messages.error(req, "Ошибка регистрации")
        except:
            messages.error(req, "Ошибка регистрации")
    context = {"form": form}
    return render(req, "main/register.html", context)
