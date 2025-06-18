from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(unique=True) 
    cpf = models.CharField(max_length=14, unique=True) # unique=True - não pode haver dois usuários com o mesmo e-mail
    criado_em = models.DateTimeField(auto_now_add=True) # auto_now_add=True - preenche automaticamente quando o objeto é criado (não muda depois).


    def __str__(self):
        return self.nome