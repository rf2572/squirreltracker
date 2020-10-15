from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .forms import SquirrelForm

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


def add(request):
    return render(request, 'sightings/add.html', {})

def pull_info(request):
    if request.method == 'POST':
            form = SquirrelForm(request.POST)
            if form.is_valid():
                form.save()
                return JsonResponse ({})
            else:
                return JsonResponse({'errors': form.errors}, status=400)

    return JsonResponse({}, status=405)
# Create your views here.
