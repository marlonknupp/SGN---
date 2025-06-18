from django.shortcuts import render, redirect 
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
