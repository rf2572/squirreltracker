# Generated by Django 3.1.2 on 2020-10-15 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sightings', '0004_auto_20201014_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squirrel',
            name='latitude',
            field=models.FloatField(blank=True, help_text='Latitude of sighting'),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='longitude',
            field=models.FloatField(blank=True, help_text='Longitude of sighting'),
        ),
    ]
