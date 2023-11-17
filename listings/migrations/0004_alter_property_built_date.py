# Generated by Django 3.2.20 on 2023-11-17 14:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='built_date',
            field=models.SmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1350), django.core.validators.MaxValueValidator(1420)]),
        ),
    ]
