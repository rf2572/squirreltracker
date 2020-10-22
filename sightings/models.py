from django.db import models
from django.utils.translation import gettext as _

class Squirrel(models.Model):
    unique_id = models.CharField(
            unique = True,
            max_length=100,
            help_text=_('Unique sighting id'),
            )

    sighting_date = models.DateField(
            help_text=_('Date of squirrel sighting'),
            blank=True,
            )

    latitude = models.FloatField(
            min_value = -90,
            max_value = 90,
            help_text=_('Latitude of sighting'),
            blank=True,
            )

    longitude = models.FloatField(
            min_value = -180,
            max_value = 180,
            help_text=_('Longitude of sighting'),
            blank=True,
            )

    SHIFT_CHOICES = [
            (AM, 'AM'),
            (PM, 'PM'),
            ]

    shift = models.CharField(
            max_length=2,
            choices=SHIFT_CHOICES,
            help_text=_('AM or PM'),
            blank=True,
            )

    AGE_CHOICES = [
            (ADULT, 'adult'),
            (JUVENILE, 'juvenile'),
            ]

    age = models.CharField(
            max_length=2,
            choices=AGE_CHOICES,
            help_text=_('Squirrel age'),
            blank=True,
            )


# Create your models here.
