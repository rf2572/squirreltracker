from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.db.models import Count

import datetime

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
   my_date = get_object_or_404(Squirrel, pk=squirrel_id).sighting_date.strftime("%Y-%m-%d")

   context = {
            'my_date':my_date,
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
    AM_count = Squirrel.objects.filter(shift='AM').count() 
    PM_count = Squirrel.objects.filter(shift='PM').count()
    YOUNGAM_count = Squirrel.objects.filter(age='juvenile', shift='AM').count()
    YOUNGPM_count = Squirrel.objects.filter(age='juvenile', shift='PM').count()
    ADULTPM_count = Squirrel.objects.filter(age='adult', shift='PM').count()
    ADULTAM_count = Squirrel.objects.filter(age='adult', shift='AM').count()
    MONTH_count = Squirrel.objects.filter(sighting_date__month="10").count()
    WEEK1_count = Squirrel.objects.filter(sighting_date__range=["2018-10-01", "2018-10-07"]).count()
    WEEK2_count = Squirrel.objects.filter(sighting_date__range=["2018-10-08", "2018-10-15"]).count()
    WEEK3_count = Squirrel.objects.filter(sighting_date__range=["2018-10-16", "2018-10-23"]).count()
    WEEK4_count = Squirrel.objects.filter(sighting_date__range=["2018-10-24", "2018-10-31"]).count()
    SOUTHEAST_count = Squirrel.objects.filter(latitude__range=["40.764408", "40.782509"], longitude__range=["-73.977393","-73.961097"]).count()
    SOUTHWEST_count = Squirrel.objects.filter(latitude__range=["40.7662625", "40.78435705"], longitude__range=["-73.981757","-73.96553525"]).count()
    NORTHEAST_count = Squirrel.objects.filter(latitude__range=["40.780661", "40.7987555"], longitude__range=["-73.965535","-73.949165"]).count()
    NORTHWEST_count = Squirrel.objects.filter(latitude__range=["40.782509", "40.800597"], longitude__range=["-73.9699735","-73.95367735"]).count()
    
    context = {
            'AM_count': AM_count, 
            'PM_count': PM_count, 
            'YOUNGPM_count': YOUNGPM_count,
            'YOUNGAM_count': YOUNGAM_count,
            'ADULTPM_count': ADULTPM_count,
            'ADULTAM_count': ADULTAM_count,
            'MONTH_count': MONTH_count, 
            'WEEK1_count': WEEK1_count,
            'WEEK2_count': WEEK2_count,
            'WEEK3_count': WEEK3_count,
            'WEEK4_count': WEEK4_count,
            'SOUTHEAST_count': SOUTHEAST_count,
            'SOUTHWEST_count': SOUTHWEST_count, 
            'NORTHWEST_count': NORTHWEST_count, 
            'NORTHEAST_count': NORTHEAST_count, 
            }
            

    return render(request, 'sightings/stats.html', context)

 
# Create your views here.
