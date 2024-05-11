from django.urls import path
from .views import ReferralList, ReferralCreate

urlpatterns = [
    path("listreferral/", ReferralList.as_view()),
    path("createreferral/", ReferralCreate.as_view()),
]
