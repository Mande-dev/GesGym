from django.db import models
from django.conf import settings
from django.utils import timezone
import uuid
from coaching.models import Coach
from organizations.models import Gym
from core.managers import GymManager


class Member(models.Model):
    """
    Représente un membre d’un gym.
    Toutes les données sont isolées par gym (multi-tenant).
    """

    STATUS_CHOICES = (
        ("active", "Active"),
        ("expired", "Expired"),
        ("suspended", "Suspended"),
    )

    # 🔐 Multi-tenant obligatoire
    gym = models.ForeignKey(
        Gym,
        on_delete=models.CASCADE,
        related_name="members",
        db_index=True
    )

    # 🔐 Manager sécurisé
    objects = GymManager()

    # lien optionnel avec User
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="member_profile",
        null=True,
        blank=True
    )

    # QR code (SANS IMAGE STOCKÉE)
    qr_code = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        db_index=True
    )

    # infos personnelles
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    photo = models.ImageField(
        upload_to="members/",
        blank=True,
        null=True
    )
    coach = models.ForeignKey(
    Coach,
    on_delete=models.SET_NULL,
    null=True,
    blank=True,
    related_name="members"
    )

    coach_notes = models.TextField(
        blank=True,
        null=True
    )
    address = models.TextField(blank=True, null=True)

    phone = models.CharField(max_length=20, db_index=True)

    email = models.EmailField(blank=True, null=True, db_index=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="active"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    
    @property
    def active_subscription(self):
        return self.subscriptions.filter(
            is_active=True
        ).select_related("plan").first()

    @property
    def expiration_date(self):
        sub = self.active_subscription
        return sub.end_date if sub else None

    @property
    def subscription_type(self):
        sub = self.active_subscription
        return sub.plan.name if sub else "Aucun"

    @property
    def last_access(self):
        log = self.access_logs.order_by("-check_in_time").first()
        return log.check_in_time if log else None

    @property
    def computed_status(self):
        if self.status == "suspended":
            return "suspended"

        today = timezone.now().date()

        active_subscription = self.subscriptions.filter(
            end_date__gte=today,
            is_active=True
        ).exists()

        if active_subscription:
            return "active"

        return "expired"

    @property
    def days_remaining(self):
        if not self.expiration_date:
            return None

        return (self.expiration_date - timezone.now().date()).days

    class Meta:
        unique_together = ("gym", "qr_code"), ("gym", "phone"), ("gym", "email")
        indexes = [

            # 🔥 performance multi-tenant
            models.Index(fields=["gym"]),

            models.Index(fields=["gym", "status"]),

            models.Index(fields=["gym", "created_at"]),
        ]
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    


class MemberAccessLog(models.Model):
    """
    Historique des accès du membre.
    """

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

    class Meta:

        indexes = [

            models.Index(fields=["member"]),

            models.Index(fields=["check_in_time"]),
            models.Index(fields=["member", "check_in_time"])
        ]