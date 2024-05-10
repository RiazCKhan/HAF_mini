from django.urls import path
from .views import ItemCreate

urlpatterns = [
    path("createitem/", ItemCreate.as_view()),
]
