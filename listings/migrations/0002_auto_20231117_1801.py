# Generated by Django 3.2.20 on 2023-11-17 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='city',
        ),
        migrations.RemoveField(
            model_name='property',
            name='province',
        ),
        migrations.RemoveField(
            model_name='property_picture',
            name='propertyid',
        ),
        migrations.RemoveField(
            model_name='property_properties',
            name='propertyid',
        ),
        migrations.DeleteModel(
            name='City',
        ),
        migrations.DeleteModel(
            name='Property',
        ),
        migrations.DeleteModel(
            name='Property_Picture',
        ),
        migrations.DeleteModel(
            name='Property_properties',
        ),
        migrations.DeleteModel(
            name='Province',
        ),
    ]
