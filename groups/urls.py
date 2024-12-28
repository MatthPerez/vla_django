from django.urls import path
from .views import GroupsView, NewGroupView, GroupUpdate, GroupDelete

urlpatterns = [
    path("", GroupsView.as_view(), name="groups"),
    path("ajouter/", NewGroupView.as_view(), name="new_group"),
    path("<int:pk>/modifier/", GroupUpdate.as_view(), name="group_update"),
    path("<int:pk>/supprimer/", GroupDelete.as_view(), name="group_delete"),
]
