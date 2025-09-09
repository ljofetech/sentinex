from django.urls import path, include

from rest_framework import routers

from .viewsets import EndpointViewSet, CheckLogViewSet

router = routers.SimpleRouter()
router.register(r"endpoint", EndpointViewSet, basename="endpoint")
router.register(r"checklog", CheckLogViewSet, basename="checklog")


urlpatterns = [
    path("", include(router.urls)),
]
