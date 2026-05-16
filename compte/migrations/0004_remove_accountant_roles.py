from django.db import migrations


def remove_accountant_roles(apps, schema_editor):
    UserGymRole = apps.get_model("compte", "UserGymRole")
    UserGymRole.objects.filter(role="accountant").delete()


class Migration(migrations.Migration):

    dependencies = [
        ("compte", "0003_create_render_superuser"),
    ]

    operations = [
        migrations.RunPython(remove_accountant_roles, migrations.RunPython.noop),
    ]
