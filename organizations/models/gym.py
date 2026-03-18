from django.db import models
from .organization import Organization


class Gym(models.Model):
    """
    Une salle de sport appartenant à une organisation.
    Toutes les données métier seront liées au Gym.
    """

    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name="gyms"
    )

    name = models.CharField(max_length=255)

    slug = models.SlugField()

    subdomain = models.CharField(
        max_length=100,
        unique=True
    )

    custom_domain = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:

        indexes = [
            models.Index(fields=["organization"]),
            models.Index(fields=["subdomain"]),
        ]

    def __str__(self):
        return self.name