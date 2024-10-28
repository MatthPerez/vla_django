from django.urls import path
from .views import InfosView

urlpatterns = [
    path("", InfosView, name="infos-index"),
]
