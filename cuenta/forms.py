from django import forms
from .models import DireccionEnvio, Artículo

class DirrecionEnvioForm(forms.ModelForm):
    class Meta:
        model = DireccionEnvio
        fields = ['telefono', 'direccion','barrio', 'observaciones']
        
class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Artículo
        fields = ['foto1', 'foto2', 'foto3', 'foto4', 'foto5', 'nombre', 'precio', 'descripcion', 'cant_disponible_XS']
