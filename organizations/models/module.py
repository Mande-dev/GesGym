from django.db import models


class Module(models.Model):
    """
    Modules activables du SaaS.
    Exemple : POS, STOCK, COACHING
    """

    code = models.CharField(max_length=50, unique=True)

    name = models.CharField(max_length=255)

    description = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name