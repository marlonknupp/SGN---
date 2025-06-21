from django.db import models
from modelo.models import Modelo
from user.models import Usuario
import datetime

class Leasing(models.Model):
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE, null=True, blank=True) # mesma lógica
    usuario = models.ForeignKey(Usuario , on_delete=models.CASCADE, null=True, blank=True)
    cidade = models.CharField(max_length=100)
    data_entrada = models.DateField(default=datetime.date.today)  # define data atual na criação
    quantidade = models.IntegerField(null=True, blank=True)
    observações = models.TextField(null=True, blank=True)
    
    ativo = models.BooleanField(default=True)
    home_office = models.BooleanField(default=False)


    def __str__(self):
        return f'{self.modelo} / {self.usuario} / {self.quantidade}'      # aparece no admin lado a lado

    
    