from django.db import models
from django.utils.translation import gettext as _

class Squirrel(models.Model):
    unique_id = models.CharField(
            max_length=100,
            help_text=_('Unique sighting id'),
            )

    sighting_date = models.DateField(
            help_text=_('Date of squirrel sighting'),
            blank=True,
            )

    # sighting_link will need to be changed

# Create your models here.
