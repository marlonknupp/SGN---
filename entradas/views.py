from django.shortcuts import render, redirect, get_object_or_404
from .models import Entrada
from .forms import EntradaForm

def lista_entradas(request):
    entradas = Entrada.objects.all()
    return render(request, 'entradas/lista.html', {'entradas': entradas})

def criar_entrada(request):
    if request.method == 'POST':
        form = EntradaForm(request.POST)
        if form.is_valid():
            entrada = form.save(commit=False)
            entrada.save()  # chama o save() do modelo que atualiza o estoque
            return redirect('lista_entrada')
    else:
        form = EntradaForm()
    return render(request, 'entradas/criar_entrada.html', {'form': form})

def ver_entrada(request, pk):
    entrada = get_object_or_404(Entrada, pk=pk)
    return render(request, 'entradas/ver.html', {'entrada': entrada})

def editar_entrada(request, pk):
    entrada = get_object_or_404(Entrada, pk=pk)
    if request.method == 'POST':
        form = EntradaForm(request.POST, instance=entrada)
        if form.is_valid():
            form.save()
            return redirect('lista_entrada')
    else:
        form = EntradaForm(instance=entrada)
    return render(request, 'entradas/form.html', {'form': form})

def deletar_entrada(request, pk):
    entrada = get_object_or_404(Entrada, pk=pk)
    if request.method == 'POST':
        entrada.delete()
        return redirect('lista_entrada')
    return render(request, 'entradas/confirmar_delete.html', {'entrada': entrada})

