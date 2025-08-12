from rest_framework.viewsets import ModelViewSet
from core.models import ClassificacaoIndicativa
from core.serializers import ClassificacaoIndicativaSerializer


class ClassificacaoIndicativaViewSet(ModelViewSet):
    queryset = ClassificacaoIndicativa.objects.all()
    serializer_class = ClassificacaoIndicativaSerializer
