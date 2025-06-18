from django.shortcuts import render, redirect
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