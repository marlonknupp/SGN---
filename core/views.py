from django.shortcuts import render
from notebook.models import Notebook
from ocorrencia.models import Ocorrencia
from user.models import Usuario
from leasing.models import Leasing
from django.db.models import Sum

def home(request):
    total_notebooks = Notebook.objects.aggregate(Sum('quantidade'))['quantidade__sum'] or 0   # soma todos da coluna quantidade de tabela # or 0 retorna 0 se nao tiver nenhum cadastrado pra nao dar erro.
    total_ocorrencias = Ocorrencia.objects.count()  # conta quantas existe no sistema
    notebooks_ativos = Leasing.objects.aggregate(Sum('quantidade'))['quantidade__sum'] or 0
    total_usuarios = Usuario.objects.count()

    return render(request, 'home.html', {
        'total_notebooks': total_notebooks,                    # Ligação com os dashbords 
        'total_ocorrencias': total_ocorrencias,
        'notebooks_ativos': notebooks_ativos,
        'total_usuarios': total_usuarios
    })




