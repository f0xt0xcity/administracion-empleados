from django import forms
from django.forms import widgets
from .models import Prueba

class PruebaForm(forms.ModelForm):

    class Meta:
        model = Prueba
        fields = (
            'titulo',
            'subtitulo',
            'cnatidad',
        )
        widgets = {
            'titulo' : forms.TextInput(
                attrs= {
                    'placeholder' : 'Ingrese texto aquí'
                }
            )
        }
    
    def clean_cnatidad(self):
        cantidad = self.cleaned_data['cnatidad']
        if cantidad < 10:
            raise forms.ValidationError("Ingresa un valor mayor a 10")
        return cantidad