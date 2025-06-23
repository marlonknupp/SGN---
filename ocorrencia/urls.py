from django.urls import path
from . import views

urlpatterns = [
    path('lista', views.lista_ocorrencia, name='lista_ocorrencia'),
    path('Nova/', views.criar_ocorrencia, name='criar_ocorrencia'),
    path('ocorrencia/<int:pk>/', views.ver_ocorrencia, name='ver_ocorrencia'),
    path('ocorrencia/<int:pk>/editar/', views.editar_ocorrencia, name='editar_ocorrencia'),
    path('ocorrencia/<int:pk>/deletar/', views.deletar_ocorrencia, name='deletar_ocorrencia'),
]