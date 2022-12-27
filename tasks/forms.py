from django.forms import ModelForm
from django import forms
from .models import Task

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'important']
        labels = {'title': 'Título', 'description': 'Descripción', 'important': 'Importante'}
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}), 'description': forms.Textarea(attrs={'class': 'form-control resize-none'}), 'important': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }

# class EditTaskForm(ModelForm):
#     class Meta:
#         model = Task
#         fields = ['title', 'description', 'important']
#         labels = {'title': 'Título', 'description': 'Descripción', 'important': 'Importante', 'datecompleted': 'Completada'}