from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task

from .forms import Taskform


def index(requst):
    tasks = Task.objects.order_by('-id')
    return render(requst, 'main/index.html',{'title':'Главная страница', 'tasks': tasks, 'author': 'author'})

def second(requst):
    return render(requst, 'main/second.html')

def create(requst):
    error = ''
    if requst.method == 'POST':
        form = Taskform(requst.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма заполнена неверно'
    form = Taskform()
    context = {'form': form,
               'error': error}
    return render(requst, 'main/create.html', context)

def four(requst):
    return render(requst, 'main/four.html')