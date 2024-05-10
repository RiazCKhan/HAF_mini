from django.urls import path
from .views import ItemCreate, ItemList, InventoryCreate, InventoryList

urlpatterns = [
    # Item
    path("listitem/", ItemList.as_view()),
    path("createitem/", ItemCreate.as_view()),
    # Inventory
    path("addinventory/", InventoryCreate.as_view()),
    path("inventory/", InventoryList.as_view()),
]
