from django.db import models


class Organization(models.Model):
    """
    Représente une entreprise cliente du SaaS.
    Une organisation peut posséder plusieurs gyms.
    """

    name = models.CharField(max_length=255)

    slug = models.SlugField(unique=True)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=["slug"]),
        ]

    def __str__(self):
        return self.name