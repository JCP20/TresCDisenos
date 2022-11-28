from django.contrib import admin
from .models import Coleccion,Artículo,CarroCompra,DireccionEnvio
# Register your models here.
admin.site.register(Coleccion)
admin.site.register(Artículo)
admin.site.register(CarroCompra)
admin.site.register(DireccionEnvio)