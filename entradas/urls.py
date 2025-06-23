from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.lista_entradas, name='lista_entrada'),
    path('nova/', views.criar_entrada, name='criar_entrada'),
    path('entradas/<int:pk>/', views.ver_entrada, name='ver_entrada'),
    path('entradas/<int:pk>/editar/', views.editar_entrada, name='editar_entrada'),
    path('entradas/<int:pk>/deletar/', views.deletar_entrada, name='deletar_entrada'),

]