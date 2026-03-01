# compte/urls.py
from django.urls import path
from . import views
from .views import CustomLoginView
from django.contrib.auth.views import LogoutView

app_name = 'compte'

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='compte:login'), name='logout'),
    #agent management
    path('create-agent/', views.create_agent, name='create_agent'),
    path('agents/', views.agent_list, name='agent_list'),
    path('agents/edit/<int:agent_id>/', views.edit_agent, name='edit_agent'),
    path('agents/delete/<int:agent_id>/', views.delete_agent, name='delete_agent'),
]