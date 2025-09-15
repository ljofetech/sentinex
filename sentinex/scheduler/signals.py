from django.db.models.signals import post_save
from django.dispatch import receiver

from django_celery_beat.models import PeriodicTask, IntervalSchedule

from .models import Endpoint, CheckLog


@receiver(post_save, sender=Endpoint)
def create_endpoint(sender, instance, created, **kwargs):
    if created:
        print("ENDPOINT IS CREATED - SIGNAL!")

        interval, _ = IntervalSchedule.objects.get_or_create(
            every=30,
            period=IntervalSchedule.SECONDS,
        )

        PeriodicTask.objects.create(
            interval=interval,
            name="endpoint-schedule",
            task="scheduler.tasks.endpoint_checker",
        )


@receiver(post_save, sender=CheckLog)
def create_checklog(sender, instance, created, **kwargs):
    if created:
        print("CHECKLOG IS CREATED - SIGNAL!")
