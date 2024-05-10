from django.urls import path
from .views import AgentList, AgentCreate, AgentUpdate

urlpatterns = [
    path("list/", AgentList.as_view()),
    path("create/", AgentCreate.as_view()),
    path("update/<int:pk>", AgentUpdate.as_view()),
]
