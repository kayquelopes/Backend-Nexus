from rest_framework import serializers
from core.models import Save

class SaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Save
        fields = ['id', 'hq']  # só envia o id da HQ

    def create(self, validated_data):
        user = self.context['request'].user  # pega o usuário logado
        return Save.objects.create(user=user, **validated_data)
