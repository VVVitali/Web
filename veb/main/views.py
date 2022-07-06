from django.shortcuts import render
from django.http import HttpResponse

def index(requst):
    return HttpResponse('<h1>First page</h1>')

def second(requst):
    return HttpResponse('<h1>&#128386</h1>')