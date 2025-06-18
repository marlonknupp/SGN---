from django.shortcuts import render, redirect
from .models import Usuario
from .forms import UsuarioForm

def lista_user(request):
    usuarios = Usuario.objects.all()
    return render (request, 'user/lista.html', {'users': usuarios})

def criar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_user')
        
    else:
        form = UsuarioForm()
    return render(request, 'user/criar_usuario.html', {'form': form})