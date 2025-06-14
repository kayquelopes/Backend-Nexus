from rest_framework.viewsets import ModelViewSet
from core.models import Status
from core.serializers import StatusSerializer

class StatusViewSet(ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer