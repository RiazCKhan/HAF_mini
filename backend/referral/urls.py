from django.urls import path
from .views import ReferralList, ReferralCreate, ReferralUpdate

urlpatterns = [
    path("listreferral/", ReferralList.as_view()),
    path("createreferral/", ReferralCreate.as_view()),
    path("updatereferral/<int:pk>", ReferralUpdate.as_view()),
]
