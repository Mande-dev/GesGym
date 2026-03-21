from django.db import models
from organizations.models import Gym
from members.models import Member
from django.core.exceptions import ValidationError


class Notification(models.Model):
    """
    Notifications envoyées aux membres
    (SMS, Email, WhatsApp).
    """

    STATUS_CHOICES = (
        ("pending", "Pending"),
        ("sent", "Sent"),
        ("failed", "Failed"),
    )

    CHANNEL_CHOICES = (
        ("sms", "SMS"),
        ("whatsapp", "WhatsApp"),
        ("email", "Email"),
    )

    gym = models.ForeignKey(
        Gym,
        on_delete=models.CASCADE,
        related_name="notifications",
        db_index=True
    )

    member = models.ForeignKey(
        Member,
        on_delete=models.CASCADE,
        related_name="notifications"
    )

    message = models.TextField()

    channel = models.CharField(
        max_length=20,
        choices=CHANNEL_CHOICES
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending"
    )

    sent_at = models.DateTimeField(
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    sent_by = models.ForeignKey(
        "compte.User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="sent_notifications"
    )

    error_message = models.TextField(blank=True, null=True)

    class Meta:

        indexes = [
            models.Index(fields=["gym"]),
            models.Index(fields=["member"]),
            models.Index(fields=["status"]),
            models.Index(fields=["gym", "status"]),
            models.Index(fields=["created_at"]),
        ]

        ordering = ["-created_at"]
    def clean(self):
        if self.member.gym != self.gym:
            raise ValidationError("Le membre n'appartient pas à ce gym.")
    def __str__(self):
        return f"{self.member} - {self.channel}"