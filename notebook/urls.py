from django.urls import path
from . import views

urlpatterns = [ 
    path('lista/', views.lista_notebook, name='lista_notebook'),
    path('notebook/<int:pk>/', views.ver_notebook, name='ver_notebook'),
]