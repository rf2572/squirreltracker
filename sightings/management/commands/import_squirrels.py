import csv
from datetime import datetime

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

            for item in reader:
                obj = Squirrel()
                obj.unique_id = item['Unique Squirrel ID']
                obj.latitude = item['Y']
                obj.longitude = item['X']
                obj.shift = item['Shift']
                obj.sighting_date = datetime.strptime(item['Date'], '%m%d%Y')
                obj.age = item['Age'].lower()

                obj.save()

        msg = f'You are importing from {file_}'

        self.stdout.write(self.style.SUCCESS(msg))
