from django.db import models
from agent.models import Agent
from client.models import Client
from item.models import Item

STATUS_CHOICES = (
    ("DRAFT", "draft"),
    ("PENDING", "pending"),
    ("APPROVED", "approved"),
    ("REQUESTED", "requested"),
    ("COMPLETE", "complete"),
)


class Referral(models.Model):  # ORDER
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="DRAFT")

    def __str__(self):
        return f"{self.id}"

    @property
    def items(self):
        return self.referralitem_set.all()


class ReferralItem(models.Model):
    referral = models.ForeignKey(
        Referral, on_delete=models.CASCADE, blank=True, null=True
    )
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.item}"
