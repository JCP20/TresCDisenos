from django import forms
from .models import DireccionEnvio

class DirrecionEnvioForm(forms.ModelForm):
    class Meta:
        model = DireccionEnvio
        fields = ['telefono', 'direccion','barrio', 'observaciones']
        