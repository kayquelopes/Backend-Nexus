from rest_framework.serializers import ModelSerializer
from core.models import HQUrl

class HQUrlSerializer(ModelSerializer):
    class Meta:
        model = HQUrl
        fields = ['id', 'hq', 'link', 'descricao']