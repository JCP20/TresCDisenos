from django.db import models


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
    precio = models.IntegerField()
    fotos = models.ImageField()
    talla = models.CharField(max_length=20)
    cant_disponible_por_talla = models.IntegerField()
    coleccion= models.ForeignKey(Coleccion, on_delete=models.SET_NULL, null=True)
    def __str__(self) -> str:
        return self.nombre