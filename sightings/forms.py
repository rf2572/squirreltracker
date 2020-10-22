from django.forms import ModelForm
from django.forms import ChoiceField
from django.forms import Select
from django.forms import DateField

from .models import Squirrel

class SquirrelForm(ModelForm):
    shift_choices = (('AM', 'AM'), ('PM', 'PM'))
    shift = ChoiceField(choices=shift_choices, label="Shift", initial='', widget=Select(), required=False)
    age_choices = (('adult', 'adult'), ('juvenile', 'juvenile'))
    age = ChoiceField(choices=age_choices, required=False)
    sighting_date = DateField(required=False)
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

class SquirrelForm2(ModelForm):
    sighting_date = DateField(required=False)
    shift_choices = (('AM', 'AM'), ('PM', 'PM'))
    shift = ChoiceField(choices=shift_choices, label="Shift", initial='', widget=Select(), required=False)
    age_choices = (('adult', 'adult'), ('juvenile', 'juvenile'))
    age = ChoiceField(choices=age_choices, required=False)
    class Meta:
        model=Squirrel
        fields = [
                'sighting_date',
                'unique_id',
                'latitude',
                'longitude',
                'shift',
                'age',
                ]
