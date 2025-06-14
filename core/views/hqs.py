from rest_framework.viewsets import ModelViewSet
from core.models import HQ
from core.serializers import HQSerializer

class HQViewSet(ModelViewSet):
    queryset = HQ.objects.all()
    serializer_class = HQSerializer
