from django.shortcuts import render
from .models import Auto


def main(request, *args, **kwargs):
    return render(request, 'task_3/base.html')

def toyota(request, *args, **kwargs):
    toyota_cars = Auto.objects.filter(name='toyota')
    return render(request, 'task_3/toyota.html', {'auto': toyota_cars})

def honda(request, *args, **kwargs):
    honda_cars = Auto.objects.filter(name='honda')
    return render(request, 'task_3/honda.html', {'auto': honda_cars})

def renault(request, *args, **kwargs):
    renault_cars = Auto.objects.filter(name='renault')
    return render(request, 'task_3/renault.html', {'auto': renault_cars})

