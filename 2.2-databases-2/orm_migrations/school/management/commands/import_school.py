import json

# from  django.utils.text import slugify
from django.core.management.base import BaseCommand
from school.models import Teacher, Student

class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('2.2-databases-2/orm_migrations/school.json', 'r', encoding='utf-8') as file:
            people = json.load(file)

        for person in people:
            if person['model'] == 'school.teacher':
                Teacher.objects.create(
                    name = person['fields']['name'],
                    subject = person['fields']['subject'],
                )
            if person['model'] == 'school.student':
                Student.objects.create(
                    name = person['fields']['name'],
                    # teachers = person['fields']['teacher'],
                    group = person['fields']['group'],
                ).teachers.add(Teacher.objects.get(pk=person['fields']['teacher']))
