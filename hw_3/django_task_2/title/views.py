from django.shortcuts import render




def display_title(request, *args, **kwargs):
    return render(request, 'title/title.html')