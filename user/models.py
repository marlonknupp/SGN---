from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(unique=True) 
    cpf = models.CharField(max_length=14, unique=True) # unique=True - não pode haver dois usuários com o mesmo e-mail
    data = models.DateTimeField(null=True, blank=True) 


    def __str__(self):
        return self.nome