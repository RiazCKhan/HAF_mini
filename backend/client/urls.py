from django.urls import path
from .views import ClientList, ClientCreate, ClientUpdate

urlpatterns = [
    path("list/", ClientList.as_view()),
    path("create/", ClientCreate.as_view()),
    path("update/<int:pk>", ClientUpdate.as_view()),
]
