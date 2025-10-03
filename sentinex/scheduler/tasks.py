import requests
import logging

from django.core.exceptions import ObjectDoesNotExist

from celery import shared_task
from requests.exceptions import RequestException

from scheduler.models import Endpoint, CheckLog

logger = logging.getLogger(__name__)


@shared_task(bind=True)
def endpoint_checker(self, endpoint_id):
    try:
        endpoint = Endpoint.objects.get(pk=endpoint_id)
    except ObjectDoesNotExist:
        logger.error(f"Endpoint with ID {endpoint_id} does not exist.")
        return

    try:
        response = requests.get(endpoint.url, timeout=10)
        is_up = response.status_code == 200
        CheckLog.objects.create(
            endpoint=endpoint,
            status_code=response.status_code,
            response_time=response.elapsed.total_seconds() * 1000,
            is_up=is_up,
        )
    except RequestException as e:
        logger.warning(f"Request failed for endpoint {endpoint.url}: {e}")
        CheckLog.objects.create(
            endpoint=endpoint,
            status_code=None,
            response_time=None,
            is_up=False,
        )
    except Exception as e:
        logger.exception(f"Unexpected error in endpoint_checker for ID {endpoint_id}")
