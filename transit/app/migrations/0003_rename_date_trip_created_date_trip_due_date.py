# Generated by Django 4.1.7 on 2023-09-25 08:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_user_user_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trip',
            old_name='date',
            new_name='created_date',
        ),
        migrations.AddField(
            model_name='trip',
            name='due_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
