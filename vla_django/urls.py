from django.contrib import admin
from django.urls import path
from .views import HomeView

from infos.views import InfosView

from groups.views import (
    GroupsView,
    NewGroupView,
    # GroupUpdate,
    # GroupDelete,
)

from persons.views import (
    PersonsView,
    PersonDetail,
    PersonCreate,
    PersonUpdate,
    PersonDelete,
)

from vcm.views import (
    VcmMeetingView,
    VcmMeetingDetail,
    NewVcmView,
    VcmUpdate,
    VcmDelete,
)

from we.views import (
    WeMeetingView,
    NewWeView,
    # WeUpdate,
    # WeDeleet,
)

from communication.views import (
    CommunicationView,
    NewCommunicationView,
    CommunicationUpdate,
    CommunicationDelete,
)

urlpatterns = [
    path("", HomeView.as_view(), name="index"),
    path("admin/", admin.site.urls),
    path("infos/", InfosView.as_view(), name="infos"),
    path("vcm/", VcmMeetingView.as_view(), name="vcm"),
    path("vcm/ajouter/", NewVcmView.as_view(), name="new_vcm"),
    path("vcm/<int:pk>/", VcmMeetingDetail.as_view(), name="vcm_detail"),
    path("vcm/<int:pk>/modifier", VcmUpdate.as_view(), name="vcm_update"),
    path("vcm/<int:pk>/suprimer", VcmDelete.as_view(), name="vcm_delete"),
    path("we/", WeMeetingView.as_view(), name="we"),
    path("we/ajouter/", NewWeView.as_view(), name="new_we"),
    path("groupes/", GroupsView.as_view(), name="groups"),
    path("groupes/ajouter/", NewGroupView.as_view(), name="new_group"),
    path("personnes/", PersonsView.as_view(), name="persons"),
    path("personnes/ajouter/", PersonCreate.as_view(), name="person_add"),
    path("personnes/<int:pk>", PersonDetail.as_view(), name="person_detail"),
    path("personnes/<int:pk>/modifier", PersonUpdate.as_view(), name="person_update"),
    path("personnes/<int:pk>/supprimer", PersonDelete.as_view(), name="person_delete"),
    path("communications/", CommunicationView.as_view(), name="communication"),
    path("communications/<int:pk>/modifier", CommunicationUpdate.as_view(), name="communication_update"),
    path("communications/<int:pk>/supprimer", CommunicationDelete.as_view(), name="communication_delete"),
    path(
        "communications/ajouter/",
        NewCommunicationView.as_view(),
        name="new_communication",
    ),
]
