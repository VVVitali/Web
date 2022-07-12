from django.shortcuts import render
from django.http import HttpResponse
from .models import Task

def index(requst):
    task = Task.objects.all()
    return render(requst, 'main/index.html',{'title':'Главная страница', 'tasks': task, 'author': 'author'})

def second(requst):
    return render(requst, 'main/second.html')