# Generated by Django 5.0.6 on 2024-05-10 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("agent", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="agent",
            name="id",
            field=models.UUIDField(primary_key=True, serialize=False),
        ),
    ]
