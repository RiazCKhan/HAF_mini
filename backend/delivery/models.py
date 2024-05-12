from django.db import models
from referral.models import Referral


STATUS_CHOICES = (
    ("DRAFT", "draft"),
    ("PENDING", "pending"),
    ("APPROVED", "approved"),
    ("REQUESTED", "requested"),
    ("COMPLETE", "complete"),
)


class Delivery(models.Model):
    referral = models.ForeignKey(Referral, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, blank=True, null=True
    )
    date = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Deliveries"
