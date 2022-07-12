from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path('sec/', views.second, name = 'second'),
    path('create', views.create, name = 'create'),
    path('four', views.four, name = 'four')
]
