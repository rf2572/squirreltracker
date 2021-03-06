# Generated by Django 3.1.2 on 2020-10-14 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sightings', '0002_squirrel_unique_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='squirrel',
            name='age',
            field=models.CharField(blank=True, help_text='Squirrel age', max_length=20),
        ),
        migrations.AddField(
            model_name='squirrel',
            name='latitude',
            field=models.CharField(blank=True, help_text='Latitude of sighting', max_length=30),
        ),
        migrations.AddField(
            model_name='squirrel',
            name='longitude',
            field=models.CharField(blank=True, help_text='Longitude of sighting', max_length=30),
        ),
        migrations.AddField(
            model_name='squirrel',
            name='shift',
            field=models.CharField(blank=True, help_text='AM or PM', max_length=2),
        ),
    ]
