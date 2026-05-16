from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("coaching", "0003_coachspecialty"),
        ("members", "0004_memberpreregistrationlink_memberpreregistration_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="GroupCoachingProgram",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=140)),
                ("objective", models.CharField(blank=True, max_length=180)),
                ("description", models.TextField(blank=True)),
                ("capacity", models.PositiveIntegerField(default=12)),
                ("is_active", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "coach",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="group_programs",
                        to="coaching.coach",
                    ),
                ),
                (
                    "gym",
                    models.ForeignKey(
                        db_index=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="group_coaching_programs",
                        to="organizations.gym",
                    ),
                ),
                (
                    "participants",
                    models.ManyToManyField(blank=True, related_name="group_coaching_programs", to="members.member"),
                ),
            ],
            options={
                "ordering": ["name"],
                "indexes": [
                    models.Index(fields=["gym", "is_active"], name="coaching_gr_gym_id_9e4c79_idx"),
                ],
                "constraints": [
                    models.UniqueConstraint(fields=("gym", "name"), name="unique_group_coaching_program_per_gym"),
                ],
            },
        ),
    ]
