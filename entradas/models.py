from django.db import models
from modelo.models import Modelo
from notebook.models import Notebook

class Entrada(models.Model):
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE, null=True, blank=True)
    quantidade = models.IntegerField()
    data_entrada = models.DateTimeField(null=True, blank=True)
    observações = models.TextField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.modelo:
            notebooks = self.modelo.notebooks.all()
            if notebooks.exists():
                
                for notebook in notebooks:
                    if notebook.quantidade is None:
                        notebook.quantidade = 0  # Corrige o valor ANTES da soma
                    notebook.quantidade += self.quantidade
                    notebook.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Entrada de {self.quantidade} Unidade(s) - {self.modelo}'
