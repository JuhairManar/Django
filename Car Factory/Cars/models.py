from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Car(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    class Meta:
        abstract = True

class ElectricCar(Car):
    battery_capacity = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} {self.model} - Electric ({self.year})"

class GasCar(Car):
    fuel_efficiency = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} {self.model} - Gas ({self.year})"
