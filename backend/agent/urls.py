from django.urls import path
from .views import AgentList

urlpatterns = [
    path("list/", AgentList.as_view()),
]
