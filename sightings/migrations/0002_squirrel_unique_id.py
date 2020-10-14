# Generated by Django 3.1.2 on 2020-10-14 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sightings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='squirrel',
            name='unique_id',
            field=models.CharField(default='default', help_text='Unique sighting id', max_length=100),
            preserve_default=False,
        ),
    ]