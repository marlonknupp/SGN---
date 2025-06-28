from django import forms
from .models import Entrada

class EntradaForm(forms.ModelForm):
    class Meta:
        model = Entrada
        fields = [ 'modelo','data_entrada', 'quantidade', 'observacoes']
        widgets = {
            'data_entrada': forms.DateInput(attrs={'type': 'date'}),  # aparece o caléndario 
        }
     