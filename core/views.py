from django.shortcuts import render
from notebook.models import Notebook
from ocorrencia.models import Ocorrencia
from user.models import Usuario
from leasing.models import Leasing
from django.db.models import Sum

def home(request):
    total_notebooks = Notebook.objects.aggregate(Sum('quantidade'))['quantidade__sum'] or 0
    total_ocorrencias = Ocorrencia.objects.count()
    notebooks_ativos = Leasing.objects.aggregate(Sum('quantidade'))['quantidade__sum'] or 0
    total_usuarios = Usuario.objects.count()

    # Filtra leasings ativos em home office
    leasings_ativos = Leasing.objects.filter(ativo=True, home_office=True)

    # Pega as cidades distintas
    cidades = leasings_ativos.values_list('cidade', flat=True).distinct()

    # Coordenadas fixas para as cidades (adicione as que precisar)
    coordenadas_cidades = {
        'sao goncalo': [-22.8268, -43.0638],
        'rio de janeiro': [-22.9068, -43.1729],
        'niteroi': [-22.8832, -43.1034],
        # outras cidades...
    }

    cidades_marcadores = []
    for cidade in cidades:
        coord = coordenadas_cidades.get(cidade.lower().strip())
        if coord:
            cidades_marcadores.append({'cidade': cidade, 'lat': coord[0], 'lng': coord[1]})


    return render(request, 'home.html', {
        'total_notebooks': total_notebooks,
        'total_ocorrencias': total_ocorrencias,
        'notebooks_ativos': notebooks_ativos,
        'total_usuarios': total_usuarios,
        'cidades_marcadores': cidades_marcadores,
    })
