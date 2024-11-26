from django.urls import path
from .views import GroupsView

urlpatterns = [
    path("", GroupsView.as_view(), name="groups-index"),
]

