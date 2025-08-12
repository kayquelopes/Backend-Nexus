from rest_framework.serializers import ModelSerializer
from core.models import ClassificacaoIndicativa

class ClassificacaoIndicativaSerializer(ModelSerializer):
    class Meta:
        model = ClassificacaoIndicativa
        fields = ['id', 'nome']