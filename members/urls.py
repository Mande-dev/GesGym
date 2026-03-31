from django.urls import path
from .views import create_member, delete_member, edit_member, member_detail, member_qr, member_list, suspend_member

app_name = "members"
urlpatterns = [
    path("", member_list, name="member_list"),
    path("create/", create_member, name="create_member"),
    path("<int:member_id>/edit/", edit_member, name="edit_member"),
    path("<int:member_id>/delete/", delete_member, name="delete_member"),
    path("<int:member_id>/suspend/", suspend_member, name="suspend_member"),
    path("<int:member_id>/", member_detail, name="member_detail"),
    path("qr/<uuid:uuid>/", member_qr, name="member_qr"),
]