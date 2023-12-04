from django.urls import path
from .views import info_city_display


urlpatterns = [
    path('', info_city_display, name='info_city_display')
]