from rest_framework.viewsets import ModelViewSet
from core.models import Idioma
from core.serializers import IdiomaSerializer

class IdiomaViewSet(ModelViewSet):
    queryset = Idioma.objects.all()
    serializer_class = IdiomaSerializer
    pagination_class = None