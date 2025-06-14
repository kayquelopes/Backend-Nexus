from django.db import models


class Idioma(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    codigo = models.CharField(max_length=10, unique=True)  # ex: pt, en, es

    def __str__(self):
        return f'{self.nome} ({self.codigo})'
