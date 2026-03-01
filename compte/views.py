# compte/views.py
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy

from .models import User
from .forms import CustomAuthenticationForm, StaffCreationForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect

class CustomLoginView(LoginView):
    template_name = 'compte/login.html'
    authentication_form = CustomAuthenticationForm

    def get_success_url(self):
        user = self.request.user

        if user.role == 'superadmin':
            return reverse_lazy('superadmin_dashboard')

        role_dashboard_map = {
            'admin': 'core:admin_dashboard',
            'manager': 'core:manager_dashboard',
            'cashier': 'core:cashier_dashboard',
            'reception': 'core:reception_dashboard',
            'member': 'core:member_dashboard',
        }

        return reverse_lazy(role_dashboard_map.get(user.role, 'compte:login'))
    
    
@login_required
def create_agent(request):

    if request.user.role != "admin":
        raise PermissionDenied("Seul l'admin peut créer des agents.")
    if request.method == "POST":
        form = StaffCreationForm(request.POST)
        if form.is_valid():
            user = form.save(gym=request.user.gym)
            messages.success(
                request,
                f"Agent créé avec succès | Username : {user.username} | Mot de passe : 12345"
            )
            return redirect("core:admin_dashboard")
    else:
        form = StaffCreationForm()

    return render(request, "compte/create_agent.html", {"form": form})


@login_required
def agent_list(request):

    if request.user.role != "admin":
        raise PermissionDenied

    agents = User.objects.filter(
        gym=request.user.gym,
        role__in=["manager", "cashier", "reception"]
    )

    return render(request, "core/admin.html", {"agents": agents})


@login_required
def edit_agent(request, agent_id):

    if request.user.role != "admin":
        raise PermissionDenied

    agent = get_object_or_404(
        User,
        id=agent_id,
        gym=request.user.gym
    )

    form = StaffCreationForm(request.POST or None, instance=agent)

    if form.is_valid():
        form.save(gym=request.user.gym)
        messages.success(request, "Agent modifié avec succès.")
        return redirect("core:admin_dashboard")

    return render(request, "compte/edit_agent.html", {"form": form})

@login_required
def delete_agent(request, agent_id):

    if request.user.role != "admin":
        raise PermissionDenied

    agent = get_object_or_404(
        User,
        id=agent_id,
        gym=request.user.gym
    )

    if request.method == "POST":
        agent.delete()
        messages.success(request, "Agent supprimé avec succès.")
        return redirect("core:admin_dashboard")

    return render(request, "compte/delete_agent.html", {"agent": agent})