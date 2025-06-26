from django.db import models
from modelo.models import Modelo
from notebook.models import Notebook

class Entrada(models.Model):
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE, null=True, blank=True)
    quantidade = models.IntegerField()
    data_entrada = models.DateTimeField(null=True, blank=True)
    observacoes = models.TextField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.pk:  # significa que já existe no banco, ou seja, é edição
            entrada_antiga = Entrada.objects.get(pk=self.pk)
            if entrada_antiga.modelo and entrada_antiga.modelo == self.modelo:
                for notebook in entrada_antiga.modelo.notebooks.all():
                    notebook.quantidade -= entrada_antiga.quantidade
                    notebook.save()

    # Agora somamos a nova quantidade normalmente
        if self.modelo:
            for notebook in self.modelo.notebooks.all():
                if notebook.quantidade is None:
                    notebook.quantidade = 0
                notebook.quantidade += self.quantidade
                notebook.save()

        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.modelo:
            for notebook in self.modelo.notebooks.all():
                if notebook.quantidade is not None:
                    notebook.quantidade -= self.quantidade
                    notebook.save()
        super().delete(*args, **kwargs)


    def __str__(self):
        return f'Entrada de {self.quantidade} Unidade(s) - {self.modelo}'
