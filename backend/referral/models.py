from django.db import models
from agent.models import Agent
from client.models import Client

STATUS_CHOICES = (
    ("DRAFT", "draft"),
    ("PENDING", "pending"),
    ("APPROVED", "approved"),
    ("REQUESTED", "requested"),
    ("COMPLETE", "complete"),
)

class Referral(models.Model):
  agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
  client = models.ForeignKey(Client, on_delete=models.CASCADE)
  status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="DRAFT")
  # item stuff
