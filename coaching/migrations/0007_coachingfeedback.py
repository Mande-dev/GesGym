from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("coaching", "0006_coachingfollowup"),
    ]

    operations = [
        migrations.CreateModel(
            name="CoachingFeedback",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("overall_rating", models.PositiveSmallIntegerField()),
                ("listening_rating", models.PositiveSmallIntegerField()),
                ("clarity_rating", models.PositiveSmallIntegerField()),
                ("motivation_rating", models.PositiveSmallIntegerField()),
                ("availability_rating", models.PositiveSmallIntegerField()),
                ("comment", models.TextField(blank=True)),
                ("wants_contact", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("coach", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="feedbacks", to="coaching.coach")),
                ("group_program", models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name="feedbacks", to="coaching.groupcoachingprogram")),
                ("gym", models.ForeignKey(db_index=True, on_delete=django.db.models.deletion.CASCADE, related_name="coaching_feedbacks", to="organizations.gym")),
                ("member", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="coaching_feedbacks", to="members.member")),
            ],
            options={
                "ordering": ["-created_at"],
                "indexes": [
                    models.Index(fields=["gym", "created_at"], name="coaching_fe_gym_id_2b6f1e_idx"),
                    models.Index(fields=["coach", "created_at"], name="coaching_fe_coach_i_ba5dc7_idx"),
                    models.Index(fields=["member", "created_at"], name="coaching_fe_member__ebc133_idx"),
                ],
            },
        ),
    ]
