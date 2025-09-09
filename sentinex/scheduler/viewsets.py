from django.shortcuts import get_object_or_404

from rest_framework import permissions, viewsets
from rest_framework.response import Response

from .models import Endpoint, CheckLog
from .serializers import EndpointSerializer, CheckLogSerializer


class EndpointViewSet(viewsets.ViewSet):
    queryset = Endpoint.objects.all()
    serializer_class = EndpointSerializer
    permission_classes = [permissions.AllowAny]

    def list(self, request):
        queryset = Endpoint.objects.all()
        serializer = EndpointSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Endpoint.objects.all()
        endpoint = get_object_or_404(queryset, pk=pk)
        serializer = EndpointSerializer(endpoint)
        return Response(serializer.data)


class CheckLogViewSet(viewsets.ViewSet):
    queryset = CheckLog.objects.all()
    serializer_class = CheckLogSerializer
    permission_classes = [permissions.AllowAny]

    def list(self, request):
        queryset = CheckLog.objects.all()
        serializer = CheckLogSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = CheckLog.objects.all()
        checklog = get_object_or_404(queryset, pk=pk)
        serializer = CheckLogSerializer(checklog)
        return Response(serializer.data)
