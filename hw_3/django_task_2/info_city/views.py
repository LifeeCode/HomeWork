from django.shortcuts import render



def info_city_display(request, *args, **kwargs):
    return render(request, 'info_city/index.html')