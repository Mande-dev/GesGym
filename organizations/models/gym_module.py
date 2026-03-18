from django.db import models
from .gym import Gym
from .module import Module


class GymModule(models.Model):
    """
    Permet d'activer un module pour un gym spécifique.
    """

    gym = models.ForeignKey(
        Gym,
        on_delete=models.CASCADE,
        related_name="modules"
    )

    module = models.ForeignKey(
        Module,
        on_delete=models.CASCADE
    )

    is_active = models.BooleanField(default=True)

    activated_at = models.DateTimeField(auto_now_add=True)

    class Meta:

        unique_together = ("gym", "module")

        indexes = [
            models.Index(fields=["gym"]),
        ]

    def __str__(self):
        return f"{self.gym} - {self.module}"