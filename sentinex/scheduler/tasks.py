import requests

from celery import shared_task

from scheduler.models import Endpoint, CheckLog


@shared_task(bind=True)
def endpoint_checker(self, endpoint_id):
    try:
        endpoint = Endpoint.objects.get(pk=endpoint_id)
        response = requests.get(endpoint.url, timeout=60)
        CheckLog.objects.create(
            endpoint=endpoint,
            status_code=int(response.status_code),
            response_time=float(response.elapsed.total_seconds() * 1000),
            is_up=True if response.status_code == 200 else False,
        )
    except Exception as e:
        print(str(e), type(e))
