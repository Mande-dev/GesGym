from django.db import models
from organizations.models import Gym


class Employee(models.Model):
    """
    Employé du gym (RH simple)
    """

    ROLE_CHOICES = (
        ("manager", "Manager"),
        ("coach", "Coach"),
        ("reception", "Accueil"),
        ("cashier", "Caissier"),
        ("cleaner", "Agent d'entretien"),
    )

    gym = models.ForeignKey(
        Gym,
        on_delete=models.CASCADE,
        related_name="employees",
        db_index=True
    )

    name = models.CharField(max_length=255)

    role = models.CharField(max_length=50, choices=ROLE_CHOICES)

    phone = models.CharField(max_length=20, blank=True, null=True)

    daily_salary = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=["gym"]),
        ]

    def __str__(self):
        return f"{self.name} - {self.role}"
    
    
class Attendance(models.Model):
    """
    Présence journalière des employés
    """

    STATUS = (
        ("present", "Présent"),
        ("absent", "Absent"),
    )

    gym = models.ForeignKey(
        Gym,
        on_delete=models.CASCADE,
        related_name="attendances",
        db_index=True
    )

    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name="attendances"
    )

    date = models.DateField()

    status = models.CharField(
        max_length=10,
        choices=STATUS,
        default="present"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("employee", "date")

        indexes = [
            models.Index(fields=["gym"]),
            models.Index(fields=["employee"]),
            models.Index(fields=["date"]),
        ]
    def calculate_salary(employee, start_date, end_date):

        attendances = employee.attendances.filter(
            date__range=(start_date, end_date),
            status="present"
        ).count()

        return attendances * employee.daily_salary
    def __str__(self):
        return f"{self.employee} - {self.date}"