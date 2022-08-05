from copyreg import add_extension
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Usuarios(models.Model):
    nombre = models.CharField(max_length=40)
    segundo_nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    dni = models.IntegerField(max_length=40)
    mail = models.EmailField(max_length=254)
    #celular = models.IntegerField(max_length=10)
    obtrasocial = models.CharField(max_length=40)

    def __str__(self):
        return self.apellido, self.nombre, self.dni


class Medicos(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    celular = models.IntegerField(max_length=10)
    edad = models.IntegerField(max_length=40)
    especialidad = models.CharField(max_length=40)

    def __str__(self):
        return self.apellido, self.nombre
