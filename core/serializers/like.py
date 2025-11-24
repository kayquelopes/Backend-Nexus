from rest_framework import serializers
from core.models import Like

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'hq']  # só envia o id da HQ

    def create(self, validated_data):
        user = self.context['request'].user  # pega o usuário logado
        return Like.objects.create(user=user, **validated_data)
