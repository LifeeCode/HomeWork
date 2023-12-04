from django.urls import path
from .views import display_city_managment

urlpatterns = [
    path('', display_city_managment, name='display_city_managment'),
]