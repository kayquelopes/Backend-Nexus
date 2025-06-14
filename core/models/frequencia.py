from django.db import models

class Frequencia(models.Model):
    nome = models.CharField(max_length=30, unique=True)  # Diária, Semanal, Mensal...
    
    def __str__(self):
        return self.nome
