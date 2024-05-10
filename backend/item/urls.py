from django.urls import path
from .views import ItemCreate, ItemList, InventoryCreate, InventoryList, InventoryUpdate

urlpatterns = [
    # Item
    path("listitem/", ItemList.as_view()),
    path("createitem/", ItemCreate.as_view()),
    # Inventory
    path("inv/", InventoryList.as_view()),
    path("addinv/", InventoryCreate.as_view()),
    path("updateinv/<int:pk>", InventoryUpdate.as_view()),
]
