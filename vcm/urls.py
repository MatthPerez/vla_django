from django.urls import path
from .views import VcmMeetingView, NewVcmView

urlpatterns = [
    path("", VcmMeetingView.as_view(), name="vcm"),
    path("ajouter/", NewVcmView.as_view(), name="new_vcm"),
]
