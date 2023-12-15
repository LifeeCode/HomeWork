from django.urls import path
from .views import headphone_info

urlpatterns = [
    path('', headphone_info, name='headphone_info'),
]

