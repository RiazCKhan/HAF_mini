from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, status

from .models import Referral
from .serializers import ReferralInfoSerializer


class ReferralList(generics.ListAPIView):
    queryset = Referral.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = ReferralInfoSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
