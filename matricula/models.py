from django.db import models

# Create your models here.

LISTA_SEXO = [

    ('Masculino', 'Masculino'),
    ('Feminino', 'Feminino'),
]
class Aluno(models.Model):
    nome = models.CharField(max_length=180)
    email = models.EmailField()
    data_de_nascimento = models.DateField()
    sexo = models.CharField(max_length=180, choices=LISTA_SEXO)

    def __str__(self):
        return self.nome