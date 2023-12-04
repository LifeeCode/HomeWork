from django.urls import path
from .views import display_city_news

urlpatterns = [
    path('', display_city_news, name='display_city_news'),
]