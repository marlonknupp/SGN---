from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_user, name='lista_user'),
    path('novo/', views.criar_usuario, name='criar_usuario'),
]

