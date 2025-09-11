from django.shortcuts import get_object_or_404

from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

from .models import NotificationConfig
from .serializers import NotificationConfigSerializer


class NotificationConfigViewSet(viewsets.ViewSet):
    queryset = NotificationConfig.objects.all()
    serializer_class = NotificationConfigSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request):
        serializer = NotificationConfigSerializer(
            data=request.data,
            context={"request": request},
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = NotificationConfig.objects.all()
        endpoint = get_object_or_404(queryset, pk=pk)
        serializer = NotificationConfigSerializer(endpoint)
        return Response(serializer.data)

    def list(self, request):
        queryset = NotificationConfig.objects.all()
        serializer = NotificationConfigSerializer(queryset, many=True)
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        endpoint = get_object_or_404(NotificationConfig, pk=pk)
        serializer = NotificationConfigSerializer(
            endpoint,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        endpoint = get_object_or_404(NotificationConfig, pk=pk)
        endpoint.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
