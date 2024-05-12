# Generated by Django 5.0.6 on 2024-05-12 21:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("delivery", "0001_initial"),
        ("referral", "0002_alter_referralitem_referral"),
    ]

    operations = [
        migrations.AddField(
            model_name="delivery",
            name="date",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="delivery",
            name="referral",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="referral.referral",
            ),
        ),
        migrations.AddField(
            model_name="delivery",
            name="status",
            field=models.CharField(
                blank=True,
                choices=[
                    ("DRAFT", "draft"),
                    ("PENDING", "pending"),
                    ("APPROVED", "approved"),
                    ("REQUESTED", "requested"),
                    ("COMPLETE", "complete"),
                ],
                max_length=10,
                null=True,
            ),
        ),
    ]