# Generated by Django 4.1 on 2022-12-10 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='pay_day',
            field=models.DateField(auto_now=True, verbose_name='last pay-day'),
        ),
        migrations.AddField(
            model_name='loader',
            name='pay_day',
            field=models.DateField(auto_now=True, verbose_name='last pay-day'),
        ),
        migrations.AddField(
            model_name='mechanic',
            name='pay_day',
            field=models.DateField(auto_now=True, verbose_name='last pay-day'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='firstName',
            field=models.CharField(max_length=20, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='lastName',
            field=models.CharField(max_length=20, verbose_name='last name'),
        ),
        migrations.AlterField(
            model_name='loader',
            name='firstName',
            field=models.CharField(max_length=20, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='loader',
            name='lastName',
            field=models.CharField(max_length=20, verbose_name='last name'),
        ),
        migrations.AlterField(
            model_name='mechanic',
            name='firstName',
            field=models.CharField(max_length=20, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='mechanic',
            name='lastName',
            field=models.CharField(max_length=20, verbose_name='last name'),
        ),
        migrations.AlterField(
            model_name='report',
            name='remark',
            field=models.CharField(max_length=25),
        ),
        migrations.DeleteModel(
            name='Message',
        ),
    ]