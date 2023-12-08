from django.shortcuts import render


def display_contacts(request, *args, **kwargs):
    return render(request, 'contacts/index.html')

