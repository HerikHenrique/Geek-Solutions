from django.db import models

# Create your models here.
#Todas as classes que herdam de models.Model são consideradas modelos do Django.
# Cada classe representa uma tabela no banco de dados.

class Todo(models.Model):
    # Cada atributo da classe representa uma coluna na tabela.
    # O tipo de dado do atributo determina o tipo de dado da coluna no banco de dados.
    title = models.CharField(max_length=100, null= False, blank=False)  # Campo de texto com tamanho máximo de 200 caracteres
    description = models.TextField()  # Campo de texto sem limite de tamanho
    completed = models.BooleanField(default=False)  # Campo booleano (True/False)
    created_at = models.DateTimeField(auto_now_add=True)  # Data e hora de criação, preenchido automaticamente
    updated_at = models.DateTimeField(auto_now=True)  # Data e hora da última atualização, preenchido automaticamente

    def __str__(self):
        return self.title  # Retorna o título do Todo como representação em string