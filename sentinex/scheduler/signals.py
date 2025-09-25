import json

from django.db.models.signals import post_save
from django.dispatch import receiver

from django_celery_beat.models import PeriodicTask, IntervalSchedule

from .models import Endpoint, CheckLog


@receiver(post_save, sender=Endpoint)
def create_endpoint(sender, instance, created, **kwargs):
    if created:
        schedule, _ = IntervalSchedule.objects.get_or_create(
            every=instance.check_interval,
            period=IntervalSchedule.SECONDS,
        )
        PeriodicTask.objects.create(
            interval=schedule,
            name=f"Monitor: {instance.url}",
            task="scheduler.tasks.endpoint_checker",
            kwargs=json.dumps(
                {
                    "endpoint_id": instance.id,
                }
            ),
        )


@receiver(post_save, sender=CheckLog)
def create_checklog(sender, instance, created, **kwargs):
    if created:
        print("CHECKLOG IS CREATED - SIGNAL!")
