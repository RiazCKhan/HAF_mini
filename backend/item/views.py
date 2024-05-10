from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, status

from .models import Item, Inventory
from .exception import InventoryException
from .serializers import (
    ItemSerializer,
    ItemInfoSerializer,
    InventorySerializer,
    InventoryInfoSerializer,
)

""" ITEM END POINTS """


class ItemList(generics.ListAPIView):
    queryset = Item.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = ItemInfoSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ItemCreate(generics.CreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )


""" INVENTORY END POINTS """


class InventoryList(generics.ListAPIView):
    queryset = Inventory.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = InventoryInfoSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class InventoryCreate(generics.CreateAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        new_inventory_item = serializer.validated_data["item"].title

        if Inventory.objects.filter(item__title=new_inventory_item).exists():
            raise InventoryException

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )


class InventoryUpdate(generics.RetrieveUpdateAPIView):
    serializer_class = InventorySerializer
    queryset = Inventory.objects.all()

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
