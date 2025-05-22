from django.db import models
from django.contrib import admin

class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    rg = models.CharField(max_length=14, unique=True)
    cpf = models.CharField(max_length=14, unique=True)
    data_cadastro = models.DateField(auto_now_add=True)
    endereco = models.CharField(max_length=255)
    telefone = models.CharField(max_length=15)
    email_cliente = models.EmailField(max_length=100, unique=True)

    def __str__(self):
        return self.nome

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email_cliente', 'telefone', 'data_cadastro')
    search_fields = ('nome', 'email_cliente')
    list_filter = ('data_cadastro',)