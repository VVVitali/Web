from .models import Task
from django.forms import ModelForm, widgets, TextInput


class Taskform(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task", "author"]
        widgets = {"title": TextInput(attrs={"class": "form-control", "placeholder": "Введите название"}),
                   "task": TextInput(attrs={"class": "form-control", "placeholder": "Введите описание"}),
                   "author": TextInput(attrs={"class": "form-control", "placeholder": "Введите имя"}),
                   }

