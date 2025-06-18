from django.db import models

class Modelo (models.Model):
    
    modelo = models.CharField(max_length=100)
    descricao = models.TextField(null=True, blank=True)
    preco = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.modelo
    
