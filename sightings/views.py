from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .forms import SquirrelForm

from .models import Squirrel
from django.core import serializers

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


def add(request):
    return render(request, 'sightings/add.html', {})

def edit(request, squirrel_id):
    squirrel = get_object_or_404(Squirrel, pk=squirrel_id)

    context = {
            'squirrel':squirrel,
            }

    if request.method == 'POST':
            form = SquirrelForm(request.POST, instance=squirrel)
            if form.is_valid():
                form.save()
                return render(request, 'sightings/edit.html', context)
            else:
                return JsonResponse({'errors': form.errors}, status=400)
    return JsonResponse({}, status=405)


def create(request):
    if request.method == 'POST':
            form = SquirrelForm(request.POST)
            if form.is_valid():
                form.save()
                return render(request, 'sightings/create.html', {})
            else:
                return JsonResponse({'errors': form.errors}, status=400)

    return JsonResponse({}, status=405)

def map(request):
    squirrels = Squirrel.objects.all()[:100]
    context = {
            'squirrels': squirrels,
            }

    return render(request, 'sightings/map.html', context)

def stats(request):
    return render(request, 'sightings/stats.html', {})

def pivot_data(request):
    dataset = Squirrel.objects.all()
    data = serializers.serialize('json', dataset,)
    return JsonResponse(data, safe=False)
    
# Create your views here.
