# Generated by Django 3.2.20 on 2023-11-12 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_auto_20231112_1237'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='propertypicture',
            name='property',
        ),
        migrations.RemoveField(
            model_name='realestateproperty',
            name='city',
        ),
        migrations.RemoveField(
            model_name='realestateproperty',
            name='pictures',
        ),
        migrations.RemoveField(
            model_name='realestateproperty',
            name='province',
        ),
        migrations.DeleteModel(
            name='City',
        ),
        migrations.DeleteModel(
            name='PropertyPicture',
        ),
        migrations.DeleteModel(
            name='Province',
        ),
        migrations.DeleteModel(
            name='RealEstateProperty',
        ),
    ]
