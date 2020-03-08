from django.db import models

# Create your models here.
class Host(models.Model):
    name = models.CharField("Nome", max_length=50)
    address = models.CharField("Endereço", max_length=100)
    city = models.CharField("Cidade", max_length=50)
    def __str__(self):
        return self.name

class Bedroom(models.Model):
    name = models.CharField("Nome", max_length=50)
    host = models.ForeignKey(Host, on_delete=models.CASCADE)
    maximum_guests = models.IntegerField("Número de hóspedes")
    busy_dates = models.TextField("Datas reservadas", blank=True)
    purchased = models.BooleanField("Vendido")
    def __str__(self):
        return self.name
