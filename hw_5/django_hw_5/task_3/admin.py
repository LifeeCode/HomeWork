from django.contrib import admin
from .models import Auto


class Categoty_autoAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Auto, Categoty_autoAdmin)
