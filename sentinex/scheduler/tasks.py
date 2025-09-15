from celery import shared_task


@shared_task
def endpoint_checker():
    print("Endpoint checker start!")
    return "Endpoint checker complete!"
