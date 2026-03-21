from django.db import models
from organizations.models import Gym
from members.models import Member
from django.core.exceptions import ValidationError

class AccessLog(models.Model):
    """
    Historique des accès des membres (scan QR, entrée gym).
    """

    gym = models.ForeignKey(
        Gym,
        on_delete=models.CASCADE,
        related_name="access_logs",
        db_index=True
    )

    member = models.ForeignKey(
        Member,
        on_delete=models.CASCADE,
        related_name="access_logs"
    )

    check_in_time = models.DateTimeField(auto_now_add=True)

    access_granted = models.BooleanField(default=True)

    device_used = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    scanned_by = models.ForeignKey(
        "compte.User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="access_scans"
    )

    class Meta:

        indexes = [
            models.Index(fields=["gym"]),
            models.Index(fields=["member"]),
            models.Index(fields=["check_in_time"]),
            models.Index(fields=["member", "check_in_time"]),
        ]

        ordering = ["-check_in_time"]

    def clean(self):
        if self.member.gym != self.gym:
            raise ValidationError("Le membre n'appartient pas à ce gym.")
    
    def __str__(self):
        return f"{self.member} - {self.check_in_time}"