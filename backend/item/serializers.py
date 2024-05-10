from rest_framework import serializers
from .models import Item, Inventory


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"


class ItemInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = "__all__"


class InventoryInfoSerializer(serializers.ModelSerializer):
    item = ItemSerializer(read_only=True)

    class Meta:
        model = Inventory
        fields = "__all__"



