# compte/urls.py
from django.urls import path
from .views import CustomLoginView, logout_view

app_name = 'compte'

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path("logout/", logout_view, name="logout"),
]