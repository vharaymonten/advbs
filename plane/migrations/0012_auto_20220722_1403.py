# Generated by Django 3.0.10 on 2022-07-22 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plane', '0011_auto_20220722_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='code',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
