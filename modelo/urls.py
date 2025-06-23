from django.urls import path # Importa a função path que usamos para criar uma rota de URL.
from . import  views         # Importa o arquivo views.py 

urlpatterns = [             # É uma lista que contém todas as rotas
    path('lista/', views.lista_modelo, name='lista_modelo'),
    path('nova/', views.criar_modelo, name='criar_modelo'),
    path('modelo/<int:pk>/', views.ver_modelo, name='ver_modelo'),
    path('modelo/<int:pk>/editar/', views.editar_modelo, name='editar_modelo'),
    path('modelo/<int:pk>/deletar/', views.deletar_modelo, name='deletar_modelo'),
]