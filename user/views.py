from django.shortcuts import render, redirect, get_object_or_404
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

def ver_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    return render(request, 'user/ver.html', {'usuario': usuario})

def editar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('lista_user')
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'user/form.html', {'form': form})

def deletar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        usuario.delete()
        return redirect('lista_usuario')
    return render(request, 'user/confirmar_delete.html', {'usuario': usuario})
