from django.shortcuts import render, redirect
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
        