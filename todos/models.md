from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20, blank=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

nome: Nome do cliente.
email: E-mail do cliente (único).
telefone: Telefone do cliente (opcional).
data_cadastro: Data/hora em que o cliente foi cadastrado.