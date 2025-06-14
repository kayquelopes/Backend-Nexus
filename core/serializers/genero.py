from rest_framework.serializers import ModelSerializer
from core.models import Genero

class GeneroSerializer(ModelSerializer):
    class Meta:
        model = Genero
        fields = ['id', 'nome']