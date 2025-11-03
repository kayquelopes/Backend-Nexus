from django.db import models
from .hqs import HQ

class HQUrl(models.Model):
    hq = models.ForeignKey(HQ, on_delete=models.CASCADE, related_name='urls')
    link = models.URLField()
    descricao = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.link