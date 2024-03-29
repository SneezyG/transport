# Generated by Django 4.1.7 on 2024-02-23 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_booking_name_alter_report_progress_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='contact1',
            field=models.CharField(max_length=20, verbose_name="Booker's contact"),
        ),
        migrations.AlterField(
            model_name='booking',
            name='contact2',
            field=models.CharField(max_length=20, verbose_name='Pick-up contact'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='contact3',
            field=models.CharField(max_length=20, verbose_name='Delivery contact'),
        ),
        migrations.AlterField(
            model_name='user',
            name='office_line',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Office-line'),
        ),
        migrations.AlterField(
            model_name='user',
            name='personal_line',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Personal-line'),
        ),
    ]
