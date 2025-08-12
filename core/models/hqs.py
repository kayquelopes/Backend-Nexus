from django.db import models
from .autor import Autor
from .genero import Genero
from .idioma import Idioma
from .status import Status
from .editora import Editora
from .frequencia import Frequencia


class HQ(models.Model):
    nome = models.CharField(max_length=255)
    autor = models.ForeignKey(Autor, on_delete=models.PROTECT)
    genero = models.ForeignKey(Genero, on_delete=models.PROTECT)
    idioma = models.ForeignKey(Idioma, on_delete=models.PROTECT)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    data_lancamento = models.DateField()
    editora = models.ForeignKey(Editora, on_delete=models.PROTECT)
    sinopse = models.TextField()
    capa = models.ImageField(upload_to='capas/')
    quantidade_capitulos = models.PositiveIntegerField()
    frequencia = models.ForeignKey(Frequencia, on_delete=models.PROTECT)
    classificacao_indicativa = models.ForeignKey('ClassificacaoIndicativa', on_delete=models.PROTECT, default=1)

    def __str__(self):
        return self.nome
