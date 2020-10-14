from django.db import models
from django.utils.translation import gettext as _

class Squirrel(models.Model):
    unique_id = models.CharField(
            max_length=100,
            help_text=_('Unique sighting id'),
            )

    sighting_date = models.CharField(
            max_length=20,
            help_text=_('Date of squirrel sighting'),
            blank=True,
            )

    latitude = models.CharField(
            max_length=30,
            help_text=_('Latitude of sighting'),
            blank=True,
            )

    longitude = models.CharField(
            max_length=30,
            help_text=_('Longitude of sighting'),
            blank=True,
            )

    shift = models.CharField(
            max_length=2,
            help_text=_('AM or PM'),
            blank=True,
            )

    age = models.CharField(
            max_length=20,
            help_text=_('Squirrel age'),
            blank=True,
            )

# Create your models here.
