from django.urls import path
from .views import WeMeetingView

urlpatterns = [
    path("", WeMeetingView, name="we-index"),
]
