from django.db import models

from scheduler.models import Endpoint


class NotificationConfig(models.Model):
    endpoint = models.ForeignKey(Endpoint, on_delete=models.CASCADE)
    telegram_chat_id = models.CharField(max_length=100)
    telegram_token = models.CharField(max_length=200)

    def __str__(self):
        return f"""
            Endpoint: {self.endpoint}
        """
