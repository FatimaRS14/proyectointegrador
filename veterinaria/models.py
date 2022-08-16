from django.db import models

from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=50,
        verbose_name="Nombre")
    presentacion = models.CharField(max_length=50,
        verbose_name="Presentación")
    precio = models.FloatField(max_length=50,
        verbose_name="Precio")
    marca = models.CharField(max_length=50,
        verbose_name="Marca")
    image = models.ImageField(upload_to='veterinaria/images/')

    def __str__(self):
        return self.nombre



class Servicio(models.Model):
    servicio = models.CharField(max_length=50,
        verbose_name="Servicio")
    descripcion = models.CharField(max_length=50,
        verbose_name="Descripción")
    texto = models.CharField(max_length=50,
        verbose_name="Texto")
    image = models.ImageField(upload_to='veterinaria/images/')

    def __str__(self):
        return self.servicio


    
