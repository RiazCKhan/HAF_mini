from django.contrib import admin
from .models import Item, Inventory


class ItemAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "category")


admin.site.register(Item, ItemAdmin)


class InventoryAdmin(admin.ModelAdmin):
    list_display = (
        "item",
        "stock",
    )


admin.site.register(Inventory, InventoryAdmin)
