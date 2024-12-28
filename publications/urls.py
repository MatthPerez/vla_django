from django.urls import path
from .views import (
    PublicationView,
    NewPublicationView,
    PublicationUpdate,
    PublicationDelete,
)

urlpatterns = [
    path("", PublicationView.as_view(), name="publications"),
    path("ajouter", NewPublicationView.as_view(), name="publication_new"),
    path("<int:pk>/modifier", PublicationUpdate.as_view(), name="publication_update"),
    path("<int:pk>/supprimer", PublicationDelete.as_view(), name="publication_delete"),
]
