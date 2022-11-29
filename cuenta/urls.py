from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('login/cuenta', views.cuenta),
    path('', views.galeria),
    path('galeria', views.galeria),
    path('tienda', views.tienda),
    path('login', views.login),
    path('registro', views.registro),
    path('login/cuenta/', views.bolsa)
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)