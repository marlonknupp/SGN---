from django import forms
from .models import Entrada
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class EntradaForm(forms.ModelForm):
    class Meta:
        model = Entrada
        fields = [ 'modelo','data_entrada', 'quantidade', 'observacoes']
        widgets = {
            'data_entrada': forms.DateInput(attrs={'type': 'date'}),  # aparece o caléndario 
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Salvar')) 