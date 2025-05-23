from django.db import models
from django.contrib.auth.models import User

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


# Create your models here.
class Repositorio(models.Model):
    OPCOES_VISIBILIDADE = (
        ('PU', 'Private'),
        ('PR', 'Public'),
    )

    nome = models.CharField(max_length=100, null=False)
    descricao = models.CharField(max_length=100, null=False)
    linguagem = models.CharField(max_length=100, null=False)
    visibilidade = models.CharField(max_length=2, choices=OPCOES_VISIBILIDADE, default='')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.nome} {self.descricao} {self.linguagem} {self.visibilidade}"
