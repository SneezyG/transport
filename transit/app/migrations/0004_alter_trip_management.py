# Generated by Django 4.1.7 on 2023-12-27 12:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_date_trip_created_date_trip_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='management',
            field=models.ForeignKey(limit_choices_to={'user_type': 'supervisor'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='trips', to=settings.AUTH_USER_MODEL),
        ),
    ]
