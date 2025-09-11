from django.urls import path, include

from rest_framework import routers

from .viewsets import NotificationConfigViewSet

router = routers.SimpleRouter()
router.register(
    r"notification-config",
    NotificationConfigViewSet,
    basename="notification-config",
)


urlpatterns = [
    path("", include(router.urls)),
]
