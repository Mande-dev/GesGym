from django.db import models
from organizations.models import Gym


class GymWebsite(models.Model):
    """
    Configuration du site public du gym
    """

    gym = models.OneToOneField(
        Gym,
        on_delete=models.CASCADE,
        related_name="website"
    )

    title = models.CharField(max_length=255)

    description = models.TextField(blank=True, null=True)

    logo = models.ImageField(
        upload_to="website/logos/",
        blank=True,
        null=True
    )

    primary_color = models.CharField(
        max_length=20,
        default="#000000"
    )

    contact_phone = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    contact_email = models.EmailField(
        blank=True,
        null=True
    )

    address = models.TextField(blank=True, null=True)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.gym.name