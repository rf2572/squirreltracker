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

    helper_date = models.CharField(
            help_text=_('Helper function'),
            max_length=20,
            blank=True,
            )

    latitude = models.FloatField(
            validators=[MinValueValidator(40.7644), MaxValueValidator(40.8006)], #uses Central Park coordinates for validation
            help_text=_('Latitude of sighting'),
            blank=True,
            )

    longitude = models.FloatField(
            validators=[MinValueValidator(-73.9818), MaxValueValidator(-73.9491)], #uses Central Park coordinates for validation
            help_text=_('Longitude of sighting'),
            blank=True,
            )
   
    def cp_location(self):
        "Returns region within Central Park"
        #southwest
        if (self.longitude <= -73.9655 and self.longitude >= -73.981):
            if (self.latitude <= 40.766 and self.latitude >= 40.784):
                return 'southwest'
        if (self.longitude <= -73.961 and self.longitude >= -73.977):
            if (self.latitude <= 40.782 and self.latitude >= 40.764):
                return 'southeast'
        if (self.longitude <= -73.953 and self.longitude >= -73.969):
            if (self.latitude <= 40.8 and self.latitude >= 40.782):
                return 'northwest'
        if (self.longitude <= -73.949 and self.longitude >= -73.965):
            if (self.latitude <= 40.798 and self.latitude >= 40.78):
                return 'northeast'

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
