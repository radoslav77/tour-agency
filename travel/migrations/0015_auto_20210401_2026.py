# Generated by Django 3.1 on 2021-04-01 19:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0014_auto_20210401_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='search',
            name='How_many_people',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
