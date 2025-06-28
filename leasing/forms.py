from django import forms
from .models import Leasing

class LeasingForm(forms.ModelForm):
    class Meta:
        model = Leasing
        fields = ['modelo','data_entrada','quantidade', 'usuario','cidade','observacoes','ativo','home_office']
        widgets = {
            'data_entrada': forms.DateInput(attrs={'type': 'date'}),  # aparece o caléndario 
        }

    
