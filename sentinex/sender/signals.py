from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import NotificationConfig


@receiver(post_save, sender=NotificationConfig)
def create_endpoint(sender, instance, created, **kwargs):
    if created:
        print("NOTIFICATION IS CREATED - SIGNAL!")
