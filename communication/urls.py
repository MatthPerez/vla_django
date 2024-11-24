from django.urls import path
from .views import CommunicationView

urlpatterns = [
    path("", CommunicationView, name="communication-index"),
]
