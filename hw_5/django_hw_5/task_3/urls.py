from django.urls import path
from .views import main, toyota, honda, renault

urlpatterns = [
    path('', main, name='main'),
    path('toyota/', toyota, name='toyota'),
    path('honda/', honda, name='honda'),
    path('renault/', renault, name='renault'),
]