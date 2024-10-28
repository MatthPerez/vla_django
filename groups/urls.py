from django.urls import path
from .views import GroupsView

urlpatterns = [
    path("", GroupsView, name="groups-index"),
]

