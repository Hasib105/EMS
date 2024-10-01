
import json
from django.core.management.base import BaseCommand
from core.models import Department

class Command(BaseCommand):
    help = 'Seed departments from a JSON file'

    def handle(self, *args, **kwargs):
        with open('db-seed/department.json') as file:
            data = json.load(file)
            for item in data:
                department, created = Department.objects.get_or_create(
                    name=item['name']
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Department "{department.name}" created.'))
                else:
                    self.stdout.write(self.style.WARNING(f'Department "{department.name}" already exists.'))