from django.db import models
from agent.models import Agent


class Client(models.Model):
    full_name = models.CharField(max_length=100)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name
