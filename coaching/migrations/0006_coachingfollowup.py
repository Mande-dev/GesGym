from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("members", "0004_memberpreregistrationlink_memberpreregistration_and_more"),
        ("organizations", "0004_organization_contact_sensitiveactivitylog"),
        ("coaching", "0005_coach_user"),
    ]

    operations = [
        migrations.CreateModel(
            name="CoachingFollowUp",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "interaction_type",
                    models.CharField(
                        choices=[
                            ("call", "Appel"),
                            ("message", "Message"),
                            ("assessment", "Bilan"),
                            ("session", "Seance"),
                            ("follow_up", "Relance"),
                        ],
                        default="follow_up",
                        max_length=20,
                    ),
                ),
                ("summary", models.TextField()),
                ("next_action", models.CharField(blank=True, max_length=255)),
                ("next_follow_up_at", models.DateField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "coach",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="follow_ups", to="coaching.coach"),
                ),
                (
                    "gym",
                    models.ForeignKey(
                        db_index=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="coaching_follow_ups",
                        to="organizations.gym",
                    ),
                ),
                (
                    "member",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="coaching_follow_ups", to="members.member"),
                ),
            ],
            options={
                "ordering": ["-created_at"],
                "indexes": [
                    models.Index(fields=["gym", "created_at"], name="coaching_fo_gym_id_f0a179_idx"),
                    models.Index(fields=["coach", "created_at"], name="coaching_fo_coach_i_c21878_idx"),
                    models.Index(fields=["member", "created_at"], name="coaching_fo_member__7ba92f_idx"),
                    models.Index(fields=["gym", "next_follow_up_at"], name="coaching_fo_gym_id_f5a329_idx"),
                ],
            },
        ),
    ]
