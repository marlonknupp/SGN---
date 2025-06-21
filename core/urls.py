from django.contrib import admin        # Importa o painel de admin do Django
from django.urls import path, include   # "path" para criar rotas, "include" para importar rotas de outros apps
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),    # mantém o acesso ao painel admin (/admin/)
    path('entradas/', include('entradas.urls')),  # ligando os app's  
    path('leasing/', include('leasing.urls')),
    path('modelo/', include ('modelo.urls')),
    path('notebook/', include('notebook.urls')),
    path('ocorrencia/', include('ocorrencia.urls')),
    path('user/', include('user.urls')),
    
]