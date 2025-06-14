from rest_framework.serializers import ModelSerializer
from core.models import Idioma

class IdiomaSerializer(ModelSerializer):
    class Meta:
        model = Idioma
        fields = ['id', 'nome']
