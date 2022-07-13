from django.shortcuts import render
from django.http import HttpResponse
from .models import Task

from .forms import Taskform


def index(requst):
    tasks = Task.objects.order_by('-id')
    return render(requst, 'main/index.html',{'title':'Главная страница', 'tasks': tasks, 'author': 'author'})

def second(requst):
    return render(requst, 'main/second.html')

def create(requst):
    form = Taskform()
    context = {'form': form}
    return render(requst, 'main/create.html', context)

def four(requst):
    return render(requst, 'main/four.html')