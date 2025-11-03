from rest_framework.viewsets import ModelViewSet
from core.models import HQUrl
from core.serializers import HQUrlSerializer

class HQUrlViewSet(ModelViewSet):
    queryset = HQUrl.objects.all()
    serializer_class = HQUrlSerializer