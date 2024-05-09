from django.db import models

class Client(models.Model):
  full_name = models.CharField()
  agent = models.ForeignKey(models.Agent, on_delete=models.CASCADE)
  phone_number = models.CharField()
  address = models.CharField()

  def __str__(self):
    return self.full_name
