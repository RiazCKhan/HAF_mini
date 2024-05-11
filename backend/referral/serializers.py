from rest_framework import serializers
from .models import Referral, ReferralItem


class ReferralItemSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = ReferralItem
        fields = (
            "id",
            "item",
            "quantity",
        )


class ReferralInfoSerializer(serializers.ModelSerializer):
    items = ReferralItemSerializer(many=True)

    class Meta:
        model = Referral
        fields = (
            "agent",
            "client",
            "status",
            "items",
        )
