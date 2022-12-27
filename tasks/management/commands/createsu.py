# tasks/management/commands/createsu.py

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Crea un superusuario.'

    def handle(self, *args, **options):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                email='panerootero@gmail.com',
                password='1972Panero1972@'
            )
        print('Superusuario ha sido creado.')