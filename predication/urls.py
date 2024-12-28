from django.urls import path
from .views import (
    PredicationView,
    NewPredicationView,
    PredicationMeetingUpdate,
    PredicationDelete,
)

urlpatterns = [
    path("", PredicationView.as_view(), name="predication"),
    path("ajouter/", NewPredicationView.as_view(), name="predication_new"),
    path(
        "<int:pk>/modifier/",
        PredicationMeetingUpdate.as_view(),
        name="predication_update",
    ),
    path("<int:pk>/supprimer/", PredicationDelete.as_view(), name="predication_delete"),
]
