from django import forms
#Cambio
from .models import Publicacion, PalabrasClave
#Fin Cambio

class PubForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = ('autor', 'Contenido')

#NUEVO
class AnalizarForm(forms.ModelForm):
    class Meta:
        model = PalabrasClave
        fields = ('Palabras',)