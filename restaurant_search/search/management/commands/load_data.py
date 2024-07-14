import csv
from django.core.management.base import BaseCommand
from search.models import Dish

class Command(BaseCommand):
    help = 'Load data from CSV file into the database'

    def handle(self, *args, **kwargs):
        with open('restaurants_small.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                Dish.objects.create(
                    id=row['id'],
                    name=row['name'],
                    location=row['location'],
                    items=row['items'],
                    lat_long=row['lat_long'],
                    full_details=row['full_details']
                )
        self.stdout.write(self.style.SUCCESS('Data loaded successfully'))
