from django.db import models


class Item(models.Model):
    title = models.CharField(unique=True, max_length=100)
    price = models.FloatField()
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Inventory(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    stock = models.IntegerField()

    def __str__(self):
        return self.item.title

    class Meta:
        verbose_name_plural = "Inventory"
