from django.db import models

class Status(models.Model):
    nome = models.CharField(max_length=50, unique=True)  # Em andamento, Finalizado

    def __str__(self):
        return self.nome