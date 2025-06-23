from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_user, name='lista_user'),
    path('novo/', views.criar_usuario, name='criar_usuario'),
    path('usuario/<int:pk>/', views.ver_usuario, name='ver_usuario'),
    path('usuario/<int:pk>/editar/', views.editar_usuario, name='editar_usuario'),
    path('usuario/<int:pk>/deletar/', views.deletar_usuario, name='deletar_usuario'),
]
