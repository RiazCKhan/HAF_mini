from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, status

from .models import Client
from .serializers import ClientSerializer


class ClientList(generics.ListAPIView):
    queryset = Client.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = ClientSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ClientCreate(generics.CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )


class ClientUpdate(generics.RetrieveUpdateAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
