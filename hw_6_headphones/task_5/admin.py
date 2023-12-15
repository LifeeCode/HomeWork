from django.contrib import admin
from .models import HeadPhone


class HeadphoneAdmin(admin.ModelAdmin):
    list_display = ['brand', 'model', 'description']



admin.site.register(HeadPhone, HeadphoneAdmin)


