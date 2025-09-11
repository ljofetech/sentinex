from django.shortcuts import get_object_or_404

from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

from .models import Endpoint, CheckLog
from .serializers import EndpointSerializer, CheckLogSerializer


class EndpointViewSet(viewsets.ViewSet):
    queryset = Endpoint.objects.all()
    serializer_class = EndpointSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request):
        serializer = EndpointSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = Endpoint.objects.all()
        endpoint = get_object_or_404(queryset, pk=pk)
        serializer = EndpointSerializer(endpoint)
        return Response(serializer.data)

    def list(self, request):
        queryset = Endpoint.objects.all()
        serializer = EndpointSerializer(queryset, many=True)
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        endpoint = get_object_or_404(Endpoint, pk=pk)
        serializer = EndpointSerializer(endpoint, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        endpoint = get_object_or_404(Endpoint, pk=pk)
        endpoint.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CheckLogViewSet(viewsets.ViewSet):
    queryset = CheckLog.objects.all()
    serializer_class = CheckLogSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request):
        serializer = CheckLogSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = CheckLog.objects.all()
        endpoint = get_object_or_404(queryset, pk=pk)
        serializer = CheckLogSerializer(endpoint)
        return Response(serializer.data)

    def list(self, request):
        queryset = CheckLog.objects.all()
        serializer = CheckLogSerializer(queryset, many=True)
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        endpoint = get_object_or_404(CheckLog, pk=pk)
        serializer = CheckLogSerializer(endpoint, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        endpoint = get_object_or_404(CheckLog, pk=pk)
        endpoint.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
