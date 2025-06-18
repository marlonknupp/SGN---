from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.lista_leasing, name='lista_leasing'),
    path('Nova/', views.location_user, name='location_user'),
]