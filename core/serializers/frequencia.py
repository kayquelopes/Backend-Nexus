from rest_framework.serializers import ModelSerializer
from core.models import Frequencia

class FrequenciaSerializer(ModelSerializer):
    class Meta:
        model = Frequencia
        fields = ['id', 'tipo']