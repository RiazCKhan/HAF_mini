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


class ReferralSerializer(serializers.ModelSerializer):
    items = ReferralItemSerializer(many=True)

    class Meta:
        model = Referral
        fields = (
            "agent",
            "client",
            "status",
            "items",
        )
            
    def create(self, validated_data):
        referral_items = validated_data.pop('items')
        print('referral items', referral_items)
        referral = Referral.objects.create(**validated_data)
        for item in referral_items:
            print('item in referral item', item)
            ReferralItem.objects.create(**item, referral=referral)
        return referral