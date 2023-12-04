from django.urls import path
from .views import display_contacts

urlpatterns = [
    path('', display_contacts, name='display_contacts')
]