from django.contrib import admin
from django.urls import path, include
from .views import HomeView
from groups.views import GroupsView
from infos.views import InfosView
from vcm.views import VcmView
from we.views import WeView

# from vcm.models import Vcm

urlpatterns = [
    path("", HomeView.as_view(), name="index"),
    path("admin/", admin.site.urls),
    path("infos/", InfosView.as_view(), name="infos"),
    path("vcm/", VcmView.as_view(), name="vcm"),
    path("we/", WeView.as_view(), name="we"),
    path("groups/", GroupsView.as_view(), name="groups"),
    # path("vcm/<str:slug>/", vcm, name="vcm"),
]

# path("infos/", include("infos.urls")),
