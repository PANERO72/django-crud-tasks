from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100, verbose_name='Título')
    description = models.TextField(blank=True, verbose_name='Descripción')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creado a')
    datecompleted = models.DateTimeField(null=True, blank=True, verbose_name='Completada:')
    important = models.BooleanField(default=False, verbose_name='Importante')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='usuario')

    def __str__(self):
        return self.title + ' - por  ' + self.user.username