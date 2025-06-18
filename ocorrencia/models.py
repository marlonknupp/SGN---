from django.db import models
from notebook.models import Notebook
from user.models import Usuario

class Ocorrencia(models.Model):
    notebook = models.ForeignKey(Notebook, on_delete=models.CASCADE, null=True, blank =True)  #ForeignKey = ligação com outra tabela
    tipo = models.CharField(max_length=50, choices=[
        ('manutenção','Manutenção'),
        ('perda', 'Perda'),
        ('defeito', 'Defeito'),
        ('outro', 'Outro'),
    ])
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, blank=True)  # ligação do campo usuario dentro de ocorrencia
    data = models.DateTimeField(null=True, blank=True)  #preenche automaticamente com o momento em que a ocorrência for criada
    observacao = models.TextField() 

    def __str__(self):
        return f'{self.tipo} - {self.notebook.nome} - {self.usuario}' # Mostra o tipo e o nome do notebook 
    