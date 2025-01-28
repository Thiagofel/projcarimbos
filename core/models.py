from django.db import models

class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=150)
    data_nascimento = models.DateField('Data')
    login = models.CharField('Login', max_length=100, default=' ')
    senha_login = models.CharField('Senha', max_length=100, default=' ')

    def __str__(self):
        return self.nome

class Carimbo(models.Model): 
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='carimbos')
    carimbo = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.carimbo} carimbos de {self.cliente.nome}"
