from django.db import models


class Auto(models.Model):
    name = models.CharField(max_length=20, verbose_name='Название марки')

    class Meta:
        db_table = 'Auto'
        verbose_name = 'Марка автомобиля'
        verbose_name_plural = 'Марки автомобиля'

    def __str__(self):
        return f'{self.name}'









