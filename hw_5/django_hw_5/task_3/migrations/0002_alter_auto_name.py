# Generated by Django 4.0 on 2023-12-10 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_3', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auto',
            name='name',
            field=models.CharField(max_length=20, verbose_name='Название марки'),
        ),
    ]