# Generated by Django 3.1.2 on 2020-10-14 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sightings', '0003_auto_20201014_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squirrel',
            name='sighting_date',
            field=models.CharField(blank=True, help_text='Date of squirrel sighting', max_length=20),
        ),
    ]
