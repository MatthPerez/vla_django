from django.urls import path
from .views import WeMeetingView, NewWeView

urlpatterns = [
    path("", WeMeetingView.as_view(), name="we"),
]
