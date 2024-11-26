from django.urls import path
from .views import InfosView

urlpatterns = [
    path("", InfosView.as_view(), name="infos-index"),
]
