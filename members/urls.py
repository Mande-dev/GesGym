from django.urls import path
from .views import member_qr

urlpatterns = [
    path("qr/<uuid:uuid>/", member_qr, name="member_qr"),
]