from django.urls import path
from .views import (
    CommunicationView,
    CommunicationUpdate,
    CommunicationDelete,
    NewCommunicationView,
)

urlpatterns = [
    path("", CommunicationView.as_view(), name="communication"),
    path("ajouter/", NewCommunicationView.as_view(), name="new_communication"),
    path(
        "<int:pk>/modifier", CommunicationUpdate.as_view(), name="communication_update"
    ),
    path(
        "<int:pk>/supprimer", CommunicationDelete.as_view(), name="communication_delete"
    ),
]
