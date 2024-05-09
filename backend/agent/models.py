from django.db import models

class Agent(models.Model):
  full_name = models.CharField()
  agency = models.CharField()
  email = models.CharField()
  phone_number = models.CharField
  status = models.BooleanField

  def __str__(self):
    return self.full_name