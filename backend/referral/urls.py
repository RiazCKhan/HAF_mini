from django.urls import path
from .views import ReferralList

urlpatterns = [
    path("listreferral/", ReferralList.as_view()),
]
