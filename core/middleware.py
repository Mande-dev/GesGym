from django.core.exceptions import PermissionDenied
from django.urls import resolve

from organizations.models import Gym

from compte.models import UserGymRole


class GymMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        request.gym = None
        request.role = None
        request.organization = None

        if request.user.is_authenticated:

            role = UserGymRole.objects.filter(
                user=request.user,
                is_active=True
            ).select_related("gym__organization").first()

            if role:
                request.gym = role.gym
                request.role = role.role
                request.organization = role.gym.organization

        return self.get_response(request)
