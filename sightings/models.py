from django.db import models
from django.utils.translation import gettext as _
from django.core.validators import MaxValueValidator, MinValueValidator

class Squirrel(models.Model):
    unique_id = models.CharField(
            unique=True,
            max_length=100,
            help_text=_('Unique sighting id'),
            )

    sighting_date = models.DateField(
            help_text=_('Date of squirrel sighting'),
            blank=True,
            )

    latitude = models.FloatField(
            validators=[MinValueValidator(-90.0), MaxValueValidator(90.0)],
            help_text=_('Latitude of sighting'),
            blank=True,
            )

    longitude = models.FloatField(
            validators=[MinValueValidator(-180.0), MaxValueValidator(180.0)],
            help_text=_('Longitude of sighting'),
            blank=True,
            )
    
    AM = 'AM'
    PM='PM'

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

    ADULT = 'adult'
    JUVENILE = 'juvenile'

    AGE_CHOICES = [
            (ADULT, 'adult'),
            (JUVENILE, 'juvenile'),
            ]

    age = models.CharField(
            max_length=10,
            choices=AGE_CHOICES,
            help_text=_('Squirrel age'),
            blank=True,
            )


# Create your models here.
