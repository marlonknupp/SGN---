from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [ 'nome','telefone', 'email','cpf','data']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),  # aparece o caléndario 
        }
        