from rest_framework import serializers
from ..models import HQ
from .autor import AutorSerializer
from .genero import GeneroSerializer
from .idioma import IdiomaSerializer
from .status import StatusSerializer
from .editora import EditoraSerializer
from .frequencia import FrequenciaSerializer
from .hqUrl import HQUrlSerializer  # importa serializer de URLs

class HQSerializer(serializers.ModelSerializer):
    autor = AutorSerializer(read_only=True)
    genero = GeneroSerializer(read_only=True)
    idioma = IdiomaSerializer(read_only=True)
    status = StatusSerializer(read_only=True)
    editora = EditoraSerializer(read_only=True)
    frequencia = FrequenciaSerializer(read_only=True)
    urls = HQUrlSerializer(many=True, read_only=True)

    capa = serializers.SerializerMethodField()  # envia a URL completa

    class Meta:
        model = HQ
        fields = [
            'id',
            'nome',
            'autor',
            'genero',
            'idioma',
            'status',
            'data_lancamento',
            'editora',
            'sinopse',
            'capa',
            'quantidade_capitulos',
            'frequencia',
            'classificacao_indicativa',
            'urls',
        ]

    def get_capa(self, obj):
        request = self.context.get('request')
        if obj.capa:
            return request.build_absolute_uri(obj.capa.url)
        return None
