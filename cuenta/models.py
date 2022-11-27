from django.db import models
from django.conf import settings
class AlbumFoto(models.Model):
    fotos = models.ImageField()
# Create your models here.
class Coleccion(models.Model):
    nombre = models.CharField(max_length=200)
    vigencia_coleccion = models.CharField(max_length=200)
    tipo_de_prenda = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.nombre
class Artículo(models.Model):
    nombre = models.CharField(max_length=200)
    tipo_articulo = models.CharField(max_length=200)
    material = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    descripcion = models.TextField()
    precio = models.FloatField()
    fotos = models.ImageField()
    cant_disponible_XS= models.IntegerField()
    cant_disponible_S= models.IntegerField()
    cant_disponible_M= models.IntegerField()
    cant_disponible_L= models.IntegerField()
    cant_disponible_XL= models.IntegerField()
    coleccion= models.ForeignKey(Coleccion, on_delete=models.SET_NULL, null=True)
    def __str__(self) -> str:
        return self.nombre
class CarroCompra(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
    items = models.ManyToManyField(Artículo)