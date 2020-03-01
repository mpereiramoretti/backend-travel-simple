from django.db import models

# Create your models here.
class Customer(models.Model):
  name = models.CharField("Name", max_length=255)
  email = models.EmailField()
  cpf = models.CharField("CPF", max_length=12)
  GENDERS = (
    ("Feminino", 'F'),
    ("Masculino", 'M'),
    ("Outro", 'O'))
  gender = models.CharField(max_length=10, choices=GENDERS)
  phone_number = models.CharField("Número de telefone", max_length=20)
  birthday = models.DateField("Data de nascimento")

  def __str__(self):
    return self.name
  