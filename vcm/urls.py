from django.urls import path
from .views import VcmMeetingView, NewVcmView

urlpatterns = [
    path("", VcmMeetingView.as_view(), name="vcm"),
]
