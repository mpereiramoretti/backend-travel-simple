from django.db import models

# Create your models here.
class Agency(models.Model):
    name = models.CharField(max_length=30)
    cnpj = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Tour(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    trip_type = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    schedules = models.CharField(max_length=30)
    def __str__(self):
        return self.name