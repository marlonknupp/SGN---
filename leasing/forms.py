from django import forms
from .models import Leasing
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class LeasingForm(forms.ModelForm):
    class Meta:
        model = Leasing
        fields = ['modelo','data_entrada','quantidade', 'usuario','cidade','observacoes','ativo','home_office']
        widgets = {
            'data_entrada': forms.DateInput(attrs={'type': 'date'}),  # aparece o caléndario 
        }

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Salvar')) 