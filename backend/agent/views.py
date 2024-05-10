from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status

from .models import Agent
from .serializers import AgentSerializer


class AgentList(generics.ListAPIView):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
