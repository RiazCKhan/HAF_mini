from django.db import models


class Donor(models.Model):
    full_name = models.CharField(max_length=100)
    foundation = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name
