from django.db import models

class Client(models.Model):
  name = models.CharField()
  agent = models.CharField()
  phone_number = models.CharField()
  address = models.CharField()
