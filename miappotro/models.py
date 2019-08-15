from django.db import models

class Libro(models.Model):
    Nombre = models.CharField(max_length=45)
    Descripcion = models.CharField(max_length=45)
    ISBN = models.CharField(max_length=45)

    def __str__ (self):
        return self.Nombre

class Prestamo(models.Model):
    Fechaprestamo = models.DateField(null=False)
    NombreCliente = models.CharField(max_length=45)
    TelefonoCliente = models.CharField(max_length=45)
    Estado = models.BooleanField(null=False)

class Ejemplar(models.Model):
    NumeroEjemplar = models.IntegerField()
    FechaCompra = models.DateField(null=False)
    Libro = models.ForeignKey(Libro, on_delete=models.CASCADE)

class DetallePrestamo(models.Model):
    Prestamo = models.ForeignKey(Prestamo, on_delete=models.CASCADE)
    Ejemplar = models.ForeignKey(Ejemplar, on_delete=models.CASCADE)


