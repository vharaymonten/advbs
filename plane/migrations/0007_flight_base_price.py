# Generated by Django 3.0.10 on 2022-07-22 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plane', '0006_merge_20220722_1212'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='base_price',
            field=models.IntegerField(default=15),
            preserve_default=False,
        ),
    ]
