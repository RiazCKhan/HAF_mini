from django.db import models


class Agent(models.Model):
    full_name = models.CharField(max_length=100)
    agency = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name
