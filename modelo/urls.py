from django.urls import path # Importa a função path que usamos para criar uma rota de URL.
from . import  views         # Importa o arquivo views.py 

urlpatterns = [             # É uma lista que contém todas as rotas
    path('lista/', views.lista_modelo, name='lista_modelo'),
    path('nova/', views.criar_modelo, name='criar_modelo'),
]