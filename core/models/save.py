from django.db import models
from core.models.user import User

class Save(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='salvos')
    hq = models.ForeignKey('HQ', on_delete=models.CASCADE, related_name='salvos')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'hq')  # impede salvar duas vezes
