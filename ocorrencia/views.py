from django.shortcuts import render, redirect, get_object_or_404
from .models import Ocorrencia
from .forms import OcorrenciaForm

def lista_ocorrencia(request):
    ocorrencia = Ocorrencia.objects.all()
    return render (request, 'ocorrencia/lista.html', {'ocorrencias': ocorrencia})

def criar_ocorrencia(request):
    if request.method == 'POST':             # verifica se a requisição foi feita com o método POST
        form = OcorrenciaForm(request.POST) 
        if form.is_valid():       # Verifica se os dados enviados passaram nas validações do formulário
            form.save()         # Salva os dados no banco de dados
            return redirect('lista_ocorrencia')
    else:
        form = OcorrenciaForm()
        return render(request, 'Ocorrencia/criar_ocorrencia.html', {'form': form})
    
def ver_ocorrencia(request, pk):
    ocorrencia = get_object_or_404(Ocorrencia, pk=pk)
    return render(request, 'ocorrencia/ver.html', {'ocorrencia': ocorrencia})

def editar_ocorrencia(request, pk):
    ocorrencia = get_object_or_404(Ocorrencia, pk=pk)
    if request.method == 'POST':
        form = OcorrenciaForm(request.POST, instance=ocorrencia)
        if form.is_valid():
            form.save()
            return redirect('lista_ocorrencia')
    else:
        form = OcorrenciaForm(instance=ocorrencia)
    return render(request, 'ocorrencia/form.html', {'form': form})

def deletar_ocorrencia(request, pk):
    ocorrencia = get_object_or_404(Ocorrencia, pk=pk)
    if request.method == 'POST':
        ocorrencia.delete()
        return redirect('lista_ocorrencia')
    return render(request, 'ocorrencia/confirmar_delete.html', {'ocorrencia': ocorrencia})
