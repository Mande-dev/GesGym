from django.db import migrations, models
import django.db.models.deletion
from django.db.models import Q


def seed_active_assignments(apps, schema_editor):
    Coach = apps.get_model("coaching", "Coach")
    CoachAssignment = apps.get_model("coaching", "CoachAssignment")

    for coach in Coach.objects.all():
        for member in coach.members.all():
            if not CoachAssignment.objects.filter(member_id=member.id, ended_at__isnull=True).exists():
                CoachAssignment.objects.create(
                    gym_id=coach.gym_id,
                    coach_id=coach.id,
                    member_id=member.id,
                )


class Migration(migrations.Migration):

    dependencies = [
        ("coaching", "0007_coachingfeedback"),
    ]

    operations = [
        migrations.CreateModel(
            name="CoachAssignment",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("started_at", models.DateTimeField(auto_now_add=True)),
                ("ended_at", models.DateTimeField(blank=True, null=True)),
                ("coach", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="assignments", to="coaching.coach")),
                ("gym", models.ForeignKey(db_index=True, on_delete=django.db.models.deletion.CASCADE, related_name="coach_assignments", to="organizations.gym")),
                ("member", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="coach_assignments", to="members.member")),
            ],
            options={
                "ordering": ["-started_at"],
                "indexes": [
                    models.Index(fields=["gym", "started_at"], name="coaching_as_gym_id_31119e_idx"),
                    models.Index(fields=["coach", "started_at"], name="coaching_as_coach_i_45df6e_idx"),
                    models.Index(fields=["member", "started_at"], name="coaching_as_member__3e1b94_idx"),
                    models.Index(fields=["gym", "ended_at"], name="coaching_as_gym_id_f70cf0_idx"),
                ],
                "constraints": [
                    models.UniqueConstraint(
                        fields=("member",),
                        condition=Q(ended_at__isnull=True),
                        name="unique_active_coach_assignment_per_member",
                    )
                ],
            },
        ),
        migrations.RunPython(seed_active_assignments, migrations.RunPython.noop),
    ]
