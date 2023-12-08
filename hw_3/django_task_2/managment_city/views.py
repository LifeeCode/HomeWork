from django.shortcuts import render


def display_city_managment(request, *args, **kwargs):
    return render(request, 'managment_city/title.html')
