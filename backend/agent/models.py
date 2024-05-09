from django.db import models

class Agent(models.Model):
  name = models.CharField()
  email = models.CharField()
  phone_number = models.CharField
  status = models.BooleanField
