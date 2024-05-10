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


class ReferralItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return self.item.title


class ReferralOrder(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    item = models.ForeignKey(ReferralItem, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.promised_items.item.title} x {self.promised_items.quantity}"


class Referral(models.Model):
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    items = models.ManyToManyField(ReferralOrder, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="DRAFT")

    def __str__(self):
        return f"Referral by: {self.agent} for {self.client}"
