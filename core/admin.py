from django.contrib import admin

from . import models


@admin.register(models.BmiMeasurement)
class BmiMeasurementAdmin(admin.ModelAdmin):
    list_display = ['height', 'weight']
