import csv
import datetime

from django.core.management.base import BaseCommand, CommandError

from sightings.models import Squirrel

class Command(BaseCommand):
    help = 'Get Squirrels into database'

    def add_arguments(self, parser):
        parser.add_argument('rows.csv', help='file containing squirrel sightings')

    def handle(self, *args, **options):
        file_ = options['rows.csv']

        with open(file_) as fp:
            reader = csv.DictReader(fp)
            
            repeats = []

            for item in reader:
                if item['Unique Squirrel ID'] not in repeats:
                    obj = Squirrel()
                    obj.unique_id = item['Unique Squirrel ID']
                    obj.latitude = item['Y']
                    obj.longitude = item['X']
                    obj.shift = item['Shift']
                    obj.sighting_date = datetime.date(int(item['Date'][4:8]), int(item['Date'][0:2]), int(item['Date'][2:4]))
                    obj.helper_date = item['Date'][4:8] + '-' + item['Date'][0:2] + '-' + item['Date'][2:4]
                    obj.age = item['Age'].lower()

                    obj.save()
                    repeats.append(item['Unique Squirrel ID'])

        msg = f'You are importing from {file_}'

        self.stdout.write(self.style.SUCCESS(msg))
