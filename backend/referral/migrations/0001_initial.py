# Generated by Django 5.0.6 on 2024-05-11 19:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("agent", "0004_alter_agent_agency_alter_agent_full_name"),
        ("client", "0002_alter_client_full_name"),
        ("item", "0002_alter_item_title"),
    ]

    operations = [
        migrations.CreateModel(
            name="Referral",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("DRAFT", "draft"),
                            ("PENDING", "pending"),
                            ("APPROVED", "approved"),
                            ("REQUESTED", "requested"),
                            ("COMPLETE", "complete"),
                        ],
                        default="DRAFT",
                        max_length=10,
                    ),
                ),
                (
                    "agent",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="agent.agent"
                    ),
                ),
                (
                    "client",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="client.client"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ReferralItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantity", models.IntegerField()),
                (
                    "item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="item.item"
                    ),
                ),
                (
                    "referral",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="referral.referral",
                    ),
                ),
            ],
        ),
    ]
