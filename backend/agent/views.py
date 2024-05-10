from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, status

from .models import Agent
from .serializers import AgentSerializer


class AgentList(generics.ListAPIView):
    queryset = Agent.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = AgentSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AgentCreate(generics.CreateAPIView):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )


class AgentUpdate(generics.RetrieveUpdateAPIView):
    serializer_class = AgentSerializer
    queryset = Agent.objects.all()

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
