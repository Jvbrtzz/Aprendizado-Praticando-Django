from django.db import models

# Create your models here.
class Dados(models.Model):
    OPCOES_USER = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    )

    nome = models.CharField(max_length=100, null=False)
    idade = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=100, null=False)   
    genero = models.CharField(max_length=1, choices=OPCOES_USER, default='')

    def __str__(self):
        return f"{self.nome} {self.idade} {self.email}"
