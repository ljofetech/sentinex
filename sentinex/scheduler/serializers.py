from rest_framework import serializers

from .models import Endpoint, CheckLog


class EndpointSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Endpoint
        fields = [
            "id",
            "name",
            "url",
            "check_interval",
            "last_checked",
            "is_active",
            "notify_on_failure",
        ]


class CheckLogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CheckLog
        fields = [
            "id",
            "endpoint",
            "status_code",
            "response_time",
            "is_up",
            "checked_at",
        ]
