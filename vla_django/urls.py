from django.contrib import admin
from django.urls import path
from .views import HomeView
from groups.views import GroupsView
from infos.views import InfosView

from vcm.views import VcmMeetingView, VcmMeetingDetail
from new_vcm_meeting.views import NewVcmView

from we.views import WeMeetingView
from new_we_meeting.views import NewWeView


urlpatterns = [
    path("", HomeView.as_view(), name="index"),
    path("admin/", admin.site.urls),
    path("infos/", InfosView.as_view(), name="infos"),
    path("vcm/", VcmMeetingView.as_view(), name="vcm"),
    path("vcm/ajouter/", NewVcmView.as_view(), name="new_vcm_meeting"),
    path("vcm/<str:date>/", VcmMeetingDetail.as_view, name="vcm-detail"),
    path("we/", WeMeetingView.as_view(), name="we"),
    path("we/ajouter/", NewWeView.as_view(), name="new_we_meeting"),
    path("groups/", GroupsView.as_view(), name="groups"),
]

# path("infos/", include("infos.urls")),
