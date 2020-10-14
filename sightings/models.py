from django.db import models
from django.utils.translation import gettext as _

class Squirrel(models.Model):
   # unique_id will need to be changed

    sighting_date = models.DateField(
            help_text=_('Date of squirrel sighting'),
            blank=True,
            )

    # sighting_link will need to be changed

# Create your models here.
