import os

from django.db import migrations


SUPERUSER_USERNAME = "rossymundyo"
SUPERUSER_PASSWORD_HASH = "pbkdf2_sha256$1200000$Bv5sjkjHkNzxaiGDM0ixlb$jX7BKbFxT08cWx6ULOo0Y8exZJisL7LR4DvZDrn73cI="


def create_render_superuser(apps, schema_editor):
    if os.environ.get("DJANGO_ENV", "development").lower() != "production":
        return

    User = apps.get_model("compte", "User")
    user, created = User.objects.get_or_create(
        username=SUPERUSER_USERNAME,
        defaults={
            "password": SUPERUSER_PASSWORD_HASH,
            "is_superuser": True,
            "is_staff": True,
            "is_active": True,
        },
    )

    update_fields = []
    if user.password != SUPERUSER_PASSWORD_HASH:
        user.password = SUPERUSER_PASSWORD_HASH
        update_fields.append("password")
    if not user.is_superuser:
        user.is_superuser = True
        update_fields.append("is_superuser")
    if not user.is_staff:
        user.is_staff = True
        update_fields.append("is_staff")
    if not user.is_active:
        user.is_active = True
        update_fields.append("is_active")

    if update_fields and not created:
        user.save(update_fields=update_fields)


class Migration(migrations.Migration):

    dependencies = [
        ("compte", "0002_user_owned_organization"),
    ]

    operations = [
        migrations.RunPython(create_render_superuser, migrations.RunPython.noop),
    ]
