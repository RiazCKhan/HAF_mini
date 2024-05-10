from django.urls import path
from .views import ItemCreate

urlpatterns = [
    path("create-item/", ItemCreate.as_view()),
]
