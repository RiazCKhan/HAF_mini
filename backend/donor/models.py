from django.db import models

class Donor(models.Model):
  full_name = models.CharField()
  foundation = models.CharField()
  email = models.CharField()
  phone_number = models.CharField()
