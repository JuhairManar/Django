from django.db import models

# Create your models here.

# class Calculation(models.Model):
#     var1=models.IntegerField()
#     var2=models.IntegerField()
#     var3=models.IntegerField(blank=True,null=True)

class Calculation(models.Model):
    var1 = models.DecimalField(max_digits=10, decimal_places=2)
    var2 = models.DecimalField(max_digits=10, decimal_places=2)
    var3 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
