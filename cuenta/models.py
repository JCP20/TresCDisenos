from django.db import models
from django.conf import settings
# Create your models here.
class Coleccion(models.Model):
    nombre = models.CharField(max_length=200)
    vigencia_coleccion = models.CharField(max_length=200)
    tipo_de_prenda = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.nombre

class Artículo(models.Model):
    nombre = models.CharField(max_length=200)
    p_sup = "Prendas superiores"
    p_inf = 'Prendas inferiores'
    tipo_articulo = models.CharField(default = p_sup, max_length=200, choices=[(p_sup,'Prendas superiores'),(p_inf,'Prendas inferiores')])
    oferta = models.BooleanField(default=False)
    material = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio = models.FloatField()
    foto1 = models.ImageField(upload_to="imagenes")
    foto2 = models.ImageField(blank=True,null=True,upload_to="imagenes")
    foto3 = models.ImageField(blank=True,null=True,upload_to="imagenes")
    foto4 = models.ImageField(blank=True,null=True,upload_to="imagenes")
    foto5 = models.ImageField(blank=True,null=True,upload_to="imagenes")
    cant_disponible_XS= models.IntegerField()
    cant_disponible_S= models.IntegerField()
    cant_disponible_M= models.IntegerField()
    cant_disponible_L= models.IntegerField()
    cant_disponible_XL= models.IntegerField()
    coleccion= models.ForeignKey(Coleccion, on_delete=models.SET_NULL, null=True)
    def __str__(self) -> str:
        return self.nombre

    def restar_cant(self):
        if self.cant_disponible_XS > 0:
            self.cant_disponible_XS -= 1
            return True
        return False

class CarroCompra(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
    items = models.ManyToManyField(Artículo)
    
class DireccionEnvio(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE,null=True)
    telefono = models.IntegerField()
    direccion = models.CharField(max_length=50)
    barrio = models.CharField(max_length=60)
    observaciones = models.TextField()
    