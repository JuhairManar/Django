from django.contrib import admin
from .models import ElectricCar, GasCar

# Register your models here.

@admin.register(ElectricCar)
class ElectricCarAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'year', 'battery_capacity', 'created', 'user')

@admin.register(GasCar)
class GasCarAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'year', 'fuel_efficiency', 'created', 'user')


