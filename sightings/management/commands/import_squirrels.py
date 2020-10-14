import csv

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
                obj.latitude = item['X']
                obj.longitude = item['Y']
                obj.shift = item['Shift']
                obj.sightings_date = item['Date']
                obj.age = item['Age']

                obj.save()

        msg = f'You are importing from {file_}'

        self.stdout.write(self.style.SUCCESS(msg))
