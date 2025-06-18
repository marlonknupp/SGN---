from django.urls import path
from . import views

urlpatterns = [
    path('lista', views.lista_ocorrencia, name='lista_ocorrencia'),
    path('Nova/', views.criar_ocorrencia, name='criar_ocorrencia'),
]