import json

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from django_celery_beat.models import PeriodicTask, IntervalSchedule

from .models import Endpoint


@receiver(post_save, sender=Endpoint)
def create_endpoint(sender, instance, created, **kwargs):
    if created:
        schedule, _ = IntervalSchedule.objects.get_or_create(
            every=instance.check_interval,
            period=IntervalSchedule.SECONDS,
        )
        PeriodicTask.objects.create(
            interval=schedule,
            name=f"Monitor: {instance.url} ({instance.id})",
            task="scheduler.tasks.endpoint_checker",
            enabled=True,
            start_time=timezone.now(),
            kwargs=json.dumps(
                {
                    "endpoint_id": instance.id,
                }
            ),
        )
