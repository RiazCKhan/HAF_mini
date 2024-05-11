from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, status

from .models import Referral
from .serializers import ReferralInfoSerializer, ReferralSerializer


class ReferralList(generics.ListAPIView):
    queryset = Referral.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = ReferralInfoSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ReferralCreate(generics.CreateAPIView):
    queryset = Referral.objects.all()
    serializer_class = ReferralSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)