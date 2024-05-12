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
            "id",
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
        referral_items = validated_data.pop("items")
        referral = Referral.objects.create(**validated_data)

        for item in referral_items:
            ReferralItem.objects.create(**item, referral=referral)
        return referral

    def update(self, instance, validated_data):
        referral_items = validated_data.pop("items")
        instance.status = validated_data.get("status", instance.status)
        instance.save()

        saved_items = []
        for item in referral_items:
            if "id" in item.keys():
                if ReferralItem.objects.filter(id=item["id"]).exists():
                    i = ReferralItem.objects.get(id=item["id"])
                    i.item = item.get("item", i.item)
                    i.quantity = item.get("quantity", i.quantity)
                    i.save()
                    saved_items.append(i.id)
                else:
                    continue
            else:
                i = ReferralItem.objects.create(**item, referral=instance)
                saved_items.append(i.id)

        for item in instance.items:
            if item.id not in saved_items:
                item.delete()

        return instance
