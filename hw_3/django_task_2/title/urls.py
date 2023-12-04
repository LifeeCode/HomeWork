from django.urls import path
from .views import display_title

urlpatterns = [
    path('', display_title, name='display_title')
]