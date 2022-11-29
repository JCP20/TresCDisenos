from django.urls import path
from . import views
urlpatterns = [
    path('cuenta', views.cuenta),
    path('', views.galeria),
    path('galeria', views.galeria),
    path('tienda', views.tienda),
    path('login', views.login),
    path('registro', views.registro),
    path('bolsa', views.bolsa),
    path('detalles', views.infoproducto)
]