from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.bolsa),
    path('', views.galeria),
    path('galeria', views.galeria),
    path('tienda', views.tienda),
    path('login', views.login),
    path('registro', views.registro),
]