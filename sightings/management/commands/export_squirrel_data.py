import csv

from django.core.management.base import BaseCommand, CommandError

from sightings.models import Squirrel

class Command(BaseCommand):
    help = 'Download sightings from the database.'

    def add_arguments(self, parser):
        parser.add_argument('rows.csv', help='name of file to export data')
    
    def handle(self, *args, **options):
        file_ = options['rows.csv']
        
        with open(file_, 'w', newline='') as fp:
             writer = csv.writer(fp)

             writer.writerow(['Unique Squirrel ID', 'Latitude', 'Longitude', 'Shift', 'Age', 'Date'])
             sightings = Squirrel.objects.all().values_list('unique_id', 'latitude', 'longitude', 'shift', 'age', 'sighting_date')
             for sighting in sightings:
                 writer.writerow(sighting)

        msg = f'Export complete.'
        return msg
