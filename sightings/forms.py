from django.forms import ModelForm

from .models import Squirrel

class SquirrelForm(ModelForm):
    class Meta:
        model = Squirrel
        fields = [
                'unique_id',
                'latitude',
                'longitude',
                'shift',
                'sighting_date',
                'age',
                ]
