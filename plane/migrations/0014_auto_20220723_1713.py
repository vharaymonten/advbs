# Generated by Django 3.0.10 on 2022-07-23 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plane', '0013_meal_airline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departure',
            name='flight_duration_m',
            field=models.IntegerField(null=True),
        ),
    ]