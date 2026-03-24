from django.contrib.auth.models import AbstractUser
from django.db import models

from organizations.models import Gym
from smartclub import settings


class User(AbstractUser):
    """
    Utilisateur du système SMARTCLUB.
    Le rôle et le gym sont gérés dans le modèle UserGymRole
    afin de permettre plusieurs rôles par utilisateur.
    """

    is_saas_admin = models.BooleanField(
        default=False,
        help_text="Administrateur global du SaaS"
    )

    def __str__(self):
        return self.username
    
class UserGymRole(models.Model):
    """
    Assigne un rôle à un utilisateur dans un gym
    """

    ROLE_CHOICES = (
        ("owner", "Owner"),
        ("manager", "Manager"),
        ("coach", "Coach"),
        ("reception", "Receptionist"),
        ("cashier", "Cashier"),
        ("accountant", "Accountant"),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="gym_roles"
    )

    gym = models.ForeignKey(
        Gym,
        on_delete=models.CASCADE,
        related_name="user_roles"
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES
    )

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "gym")

        indexes = [
            models.Index(fields=["gym"]),
            models.Index(fields=["user"]),
            models.Index(fields=["user", "gym"])
        ]

    def __str__(self):
        return f"{self.user} - {self.role} ({self.gym})"