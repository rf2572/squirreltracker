from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Squirrel

def index(request):
    squir = Squirrel.objects.all()
    context = {
            'Squirrels': squir,
            }

    return render(request, 'sightings/index.html', context)

def detail(request, squirrel_id):
    squirrel = get_object_or_404(Squirrel, pk=squirrel_id)

    context = {
            'Squirrel':squirrel,        
            }
    return render(request, 'sightings/detail.html', context)

# Create your views here.
