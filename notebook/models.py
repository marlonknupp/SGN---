from django.db import models
from modelo.models import Modelo       #importando a relação do modelo dentro do noteboks na hora de criar 

class Notebook(models.Model):
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE, null=True, blank=True, related_name='notebooks')  # relacionando a opção modelo dentro do notebook na hora de cadastrar e importando la em cima
    quantidade = models.IntegerField(null=True, blank=True, default=0)
    

    def __str__(self):
        return str(self.modelo)