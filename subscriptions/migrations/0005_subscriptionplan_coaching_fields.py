from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("subscriptions", "0004_subscriptionrequest"),
    ]

    operations = [
        migrations.AddField(
            model_name="subscriptionplan",
            name="coaching_level",
            field=models.CharField(
                choices=[
                    ("standard", "Standard"),
                    ("premium", "Premium"),
                    ("intensive", "Intensif"),
                ],
                default="standard",
                max_length=20,
            ),
        ),
        migrations.AddField(
            model_name="subscriptionplan",
            name="coaching_mode",
            field=models.CharField(
                choices=[
                    ("none", "Aucun coaching"),
                    ("individual", "Coaching individuel"),
                    ("group", "Programme groupe"),
                    ("both", "Coaching individuel et groupe"),
                ],
                default="none",
                max_length=20,
            ),
        ),
    ]
