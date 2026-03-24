from django.urls import path
from .views import gym_home

urlpatterns = [
    path("", gym_home, name="gym_home"),
]