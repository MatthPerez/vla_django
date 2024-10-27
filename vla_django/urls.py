from django.contrib import admin
from django.urls import path, include
from .views import index

# from vcm.models import Vcm

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("infos/", include("infos.urls")),
    path("vcm/", include("vcm.urls")),
    path("we/", include("we.urls")),
    path("groups/", include("groups.urls")),
    # path("vcm/<str:slug>/", vcm, name="vcm"),
]
