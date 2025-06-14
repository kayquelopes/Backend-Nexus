from rest_framework.viewsets import ModelViewSet
from core.models import Frequencia
from core.serializers import FrequenciaSerializer

class FrequenciaViewSet(ModelViewSet):
    queryset = Frequencia.objects.all()
    serializer_class = FrequenciaSerializer