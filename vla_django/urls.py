from django.contrib import admin
from django.urls import path
from .views import HomeView

from infos.views import InfosView

from groups.views import (
    GroupsView,
    NewGroupView,
    GroupUpdate,
    GroupDelete,
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
    WeUpdate,
    WeDelete,
)

from communication.views import (
    CommunicationView,
    NewCommunicationView,
    CommunicationUpdate,
    CommunicationDelete,
)

from predication.views import (
    PredicationView,
    NewPredicationView,
    PredicationMeetingUpdate,
    PredicationDelete,
)

from publications.views import (
    PublicationView,
    NewPublicationView,
    PublicationUpdate,
    PublicationDelete,
)

from commands.views import (
    CommandsView,
    NewCommandView,
    CommandUpdate,
    CommandDelete,
)

from accounts.views import Signup, Signin, Logout

from private.views import PrivateView

from notes.views import (
    NewNote,
    NoteUpdate,
    NoteDelete,
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
    path("we/<int:pk>/modifier", WeUpdate.as_view(), name="we_update"),
    path("we/<int:pk>/supprimer", WeDelete.as_view(), name="we_delete"),
    path("groupes/", GroupsView.as_view(), name="groups"),
    path("groupes/ajouter/", NewGroupView.as_view(), name="new_group"),
    path("groupes/<int:pk>/modifier/", GroupUpdate.as_view(), name="group_update"),
    path("groupes/<int:pk>/supprimer/", GroupDelete.as_view(), name="group_delete"),
    path("personnes/", PersonsView.as_view(), name="persons"),
    path("personnes/ajouter/", PersonCreate.as_view(), name="person_add"),
    path("personnes/<int:pk>", PersonDetail.as_view(), name="person_detail"),
    path("personnes/<int:pk>/modifier/", PersonUpdate.as_view(), name="person_update"),
    path("personnes/<int:pk>/supprimer/", PersonDelete.as_view(), name="person_delete"),
    path("communications/", CommunicationView.as_view(), name="communication"),
    path(
        "communications/<int:pk>/modifier",
        CommunicationUpdate.as_view(),
        name="communication_update",
    ),
    path(
        "communications/<int:pk>/supprimer",
        CommunicationDelete.as_view(),
        name="communication_delete",
    ),
    path(
        "communications/ajouter/",
        NewCommunicationView.as_view(),
        name="new_communication",
    ),
    path("predication/", PredicationView.as_view(), name="predication"),
    path("predication/ajouter/", NewPredicationView.as_view(), name="predication_new"),
    path(
        "predication/<int:pk>/modifier/",
        PredicationMeetingUpdate.as_view(),
        name="predication_update",
    ),
    path(
        "predication/<int:pk>/supprimer/",
        PredicationDelete.as_view(),
        name="predication_delete",
    ),
    path("publications/", PublicationView.as_view(), name="publications"),
    path("publications/ajouter", NewPublicationView.as_view(), name="publication_new"),
    path(
        "publications/<int:pk>/modifier",
        PublicationUpdate.as_view(),
        name="publication_update",
    ),
    path(
        "publications/<int:pk>/supprimer",
        PublicationDelete.as_view(),
        name="publication_delete",
    ),
    path(
        "commandes/",
        CommandsView.as_view(),
        name="commands",
    ),
    path(
        "commandes/ajouter/",
        NewCommandView.as_view(),
        name="command_new",
    ),
    path(
        "commandes/<int:pk>/modifier/",
        CommandUpdate.as_view(),
        name="command_update",
    ),
    path(
        "commandes/<int:pk>/supprimer/",
        CommandDelete.as_view(),
        name="command_delete",
    ),
    path(
        "inscription/",
        Signup.as_view(),
        name="signup",
    ),
    path(
        "connexion/",
        Signin.as_view(),
        name="signin",
    ),
    path(
        "deconnexion/",
        Logout.as_view(),
        name="logout",
    ),
    path(
        "ma_page/",
        PrivateView.as_view(),
        name="private",
    ),
    path(
        "ma_page/note/",
        NewNote.as_view(),
        name="note_new",
    ),
    path(
        "ma_page/note/<int:pk>/modifier",
        NoteUpdate.as_view(),
        name="note_update",
    ),
    path(
        "ma_page/note/<int:pk>/supprimer",
        NoteDelete.as_view(),
        name="note_delete",
    ),
]
