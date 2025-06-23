from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.lista_leasing, name='lista_leasing'),
    path('Nova/', views.location_user, name='location_user'),
    path('leasing/<int:pk>/', views.ver_leasing, name='ver_leasing'),
    path('leasing/<int:pk>/editar/', views.editar_leasing, name='editar_leasing'),
    path('leasing/<int:pk>/deletar/', views.deletar_leasing, name='deletar_leasing'),
]