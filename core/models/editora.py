from django.db import models

class Editora(models.Model):
    nome = models.CharField(max_length=255, unique=True)
    
    def __str__(self):
        return self.nome
