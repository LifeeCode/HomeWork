from django.shortcuts import render


def display_city_news(request, *args, **kwargs):
    return render(request, 'city_news/title.html')

