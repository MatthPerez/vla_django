from django.contrib import admin
from django.urls import path
from .views import HomeView
from infos.views import InfosView

from groups.views import GroupsView
from new_group.views import NewGroupView

from persons.views import PersonsView, PersonsDetail
from new_person.views import NewPersonView

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
    path("vcm/<pk>/", VcmMeetingDetail.as_view(), name="vcm-detail"),
    path("we/", WeMeetingView.as_view(), name="we"),
    path("we/ajouter/", NewWeView.as_view(), name="new_we_meeting"),
    path("groupes/", GroupsView.as_view(), name="groups"),
    path("groupes/ajouter/", NewGroupView.as_view(), name="new_group"),
    # path("groupes/<pk>", GroupsDetail.as_view(), name="group-detail"),
    path("personnes/", PersonsView.as_view(), name="persons"),
    path("personnes/ajouter/", NewPersonView.as_view(), name="new-person"),
    path("personnes/<pk>", PersonsDetail.as_view(), name="person-detail"),
]
