# Generated by Django 4.1.7 on 2024-02-03 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_report_latitude_alter_report_longitude'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='session_key',
            field=models.TextField(default=''),
        ),
    ]
