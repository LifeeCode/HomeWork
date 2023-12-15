# Generated by Django 4.0 on 2023-12-14 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HeadPhone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=20, verbose_name='Бренд>')),
                ('model', models.CharField(max_length=20, verbose_name='Модель')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'db_table': 'Наушники',
            },
        ),
    ]
