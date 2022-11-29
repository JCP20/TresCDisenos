from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('panel_usuario', views.panel_usuario, name= "panel_usuario"),
    path('', views.galeria),
    path('galeria', views.galeria),
    path('tienda', views.tienda),
    path('login', views.login),
    path('registro', views.registro),
    path('bolsa', views.bolsa),
    path('detalles', views.infoproducto)
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)