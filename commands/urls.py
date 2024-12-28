from django.urls import path
from .views import CommandsView, NewCommandView, CommandUpdate, CommandDelete

urlpatterns = [
    path("", CommandsView.as_view(), name="commands"),
    path("ajouter/", NewCommandView.as_view(), name="command_new"),
    path("<int:pk>/modifier/", CommandUpdate.as_view(), name="command_update"),
    path("<int:pk>/supprimer/", CommandDelete.as_view(), name="command_delete"),
]
