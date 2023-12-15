from django.db import models



class HeadPhone(models.Model):

    brand = models.CharField(max_length=20, verbose_name='Бренд')
    model = models.CharField(max_length=20, verbose_name='Модель')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        db_table = 'Наушники'

    def __str__(self):
        return self.model
