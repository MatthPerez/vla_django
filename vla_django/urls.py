from django.contrib import admin
from django.urls import path
from .views import HomeView
from groups.views import GroupsView
from infos.views import InfosView
from vcm.views import VcmMeetingView
from we.views import WeView


urlpatterns = [
    path("", HomeView.as_view(), name="index"),
    path("admin/", admin.site.urls),
    path("infos/", InfosView.as_view(), name="infos"),
    path("vcm/", VcmMeetingView.as_view(), name="vcm"),
    # path("vcm/<str:slug>/", VcmMeetingView, name="vcm"),
    path("we/", WeView.as_view(), name="we"),
    path("groups/", GroupsView.as_view(), name="groups"),
]

# path("infos/", include("infos.urls")),
