from rest_framework import serializers
from ..models import HQ
from .autor import AutorSerializer
from .genero import GeneroSerializer
from .idioma import IdiomaSerializer
from .status import StatusSerializer
from .editora import EditoraSerializer
from .frequencia import FrequenciaSerializer

class HQSerializer(serializers.ModelSerializer):
    autor = AutorSerializer(read_only=True)
    genero = GeneroSerializer(read_only=True)
    idioma = IdiomaSerializer(read_only=True)
    status = StatusSerializer(read_only=True)
    editora = EditoraSerializer(read_only=True)
    frequencia = FrequenciaSerializer(read_only=True)
    

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
        ]
