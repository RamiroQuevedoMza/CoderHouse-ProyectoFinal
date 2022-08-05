from copyreg import add_extension
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Usuarios(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.CharField(max_length=40)
    mail = models.EmailField()

class Medicos(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.CharField(max_length=40)
    especialidad = models.CharField(max_length=40)


        