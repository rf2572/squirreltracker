from django.forms import ModelForm
from django.forms import ChoiceField
from django.forms import Select
from django.forms import DateField
from django.forms import FloatField

from .models import Squirrel

class SquirrelForm(ModelForm):
    shift_choices = (('AM', 'AM'), ('PM', 'PM'))
    shift = ChoiceField(choices=shift_choices, label="Shift", initial='', widget=Select(), required=False)
    age_choices = (('adult', 'adult'), ('juvenile', 'juvenile'))
    age = ChoiceField(choices=age_choices, required=False)
    sighting_date = DateField(required=False)
    longitude = FloatField(required=False)
    latitude = FloatField(required=False)
    class Meta:
        model = Squirrel
        fields = [
                'sighting_date',
                'unique_id',
                'latitude',
                'longitude',
                'shift',
                'age',
                'helper_date',
                ]


