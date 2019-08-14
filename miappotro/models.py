from django.db import models

class Libro(models.Model):
    Nombre = models.CharField(max_length=45)
    Descripcion = models.CharField(max_length=45)
    ISBN = models.CharField(max_length=45)

