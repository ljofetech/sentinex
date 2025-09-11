from rest_framework import serializers

from .models import NotificationConfig


class NotificationConfigSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NotificationConfig
        fields = [
            "id",
            "endpoint",
            "telegram_chat_id",
            "telegram_token",
        ]
