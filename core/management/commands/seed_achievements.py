import json
from django.core.management.base import BaseCommand
from core.models import Achievement

class Command(BaseCommand):
    help = 'Seed achievements from a JSON file'

    def handle(self, *args, **kwargs):
        with open('db-seed/achievement.json') as file:
            data = json.load(file)
            for item in data:
                achievement, created = Achievement.objects.get_or_create(
                    name=item['name']
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Achievement "{achievement.name}" created.'))
                else:
                    self.stdout.write(self.style.WARNING(f'Achievement "{achievement.name}" already exists.'))