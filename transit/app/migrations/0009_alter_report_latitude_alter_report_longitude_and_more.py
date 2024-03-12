# Generated by Django 4.1.7 on 2024-02-04 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_user_session_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='latitude',
            field=models.DecimalField(decimal_places=6, max_digits=9),
        ),
        migrations.AlterField(
            model_name='report',
            name='longitude',
            field=models.DecimalField(decimal_places=6, default=50, max_digits=9),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='report',
            name='status',
            field=models.CharField(choices=[('G', 'Green'), ('R', 'Red'), ('Y', 'Yellow')], max_length=2),
        ),
    ]