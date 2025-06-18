from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.lista_entradas, name='lista_entrada'),
    path('nova/', views.criar_entrada, name='criar_entrada'),

]