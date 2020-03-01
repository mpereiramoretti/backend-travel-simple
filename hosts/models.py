from django.db import models

# Create your models here.
class Host(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    bedroom_name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    available_places = models.IntegerField()
    busy_dates = models.DateField("Busy dates")
    purchased = models.BooleanField()
    def __str__(self):
        return self.name