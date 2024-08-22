from django.contrib import admin
from django.urls import path, include
from . import views
from . import user_views

urlpatterns = [
    path("", views.index, name="home"),
    path("game/<slug:token>", views.connect_to_game, name="connect_to_game"),
    # path("game/new", views.start_new_game, name="start_new_game"),
    ###
    path("login", user_views.loginPage, name="login"),
    path("logout", user_views.logoutPage, name="logout"),
    path("register", user_views.registerPage, name="register"),
]
