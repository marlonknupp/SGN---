from django import forms
from .models import Usuario
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [ 'nome','telefone', 'email','cpf','data']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),  # aparece o caléndario 
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Salvar')) 