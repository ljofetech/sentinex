from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Endpoint, CheckLog


@receiver(post_save, sender=Endpoint)
def create_endpoint(sender, instance, created, **kwargs):
    if created:
        print("ENDPOINT IS CREATED - SIGNAL!")


@receiver(post_save, sender=CheckLog)
def create_checklog(sender, instance, created, **kwargs):
    if created:
        print("CHECKLOG IS CREATED - SIGNAL!")
