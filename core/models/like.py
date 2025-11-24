from django.db import models
from core.models.user import User

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='curtidas')
    hq = models.ForeignKey('HQ', on_delete=models.CASCADE, related_name='curtidas')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'hq')  # impede curtir duas vezes
