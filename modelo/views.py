from django.shortcuts import render, redirect, get_object_or_404
from .models import Modelo
from .forms import ModeloForm

def lista_modelo(request):
    modelos = Modelo.objects.all()
    return render(request, 'modelo/lista.html', {'modelos': modelos})

def criar_modelo(request):
    if request.method == 'POST':
        form = ModeloForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Lista_modelo')
    
    else:
        form = ModeloForm()
    return render(request, 'modelo/criar_modelo.html', {'form': form})

def ver_modelo(request, pk):
    modelo = get_object_or_404(Modelo, pk=pk)
    return render(request, 'modelo/ver.html', {'modelo': modelo})

def editar_modelo(request, pk):
    modelo = get_object_or_404(Modelo, pk=pk)
    if request.method == 'POST':
        form = ModeloForm(request.POST, instance=modelo)
        if form.is_valid():
            form.save()
            return redirect('lista_modelo')
    else:
        form = ModeloForm(instance=modelo)
    return render(request, 'modelo/form.html', {'form': form})

def deletar_modelo(request, pk):
    modelo = get_object_or_404(Modelo, pk=pk)
    if request.method == 'POST':
        Modelo.delete()
        return redirect('lista_modelo')
    return render(request, 'modelo/confirmar_delete.html', {'modelo': modelo})
