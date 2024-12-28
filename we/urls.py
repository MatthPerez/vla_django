from django.urls import path
from .views import WeMeetingView, NewWeView, WeUpdate, WeDelete

urlpatterns = [
    path("", WeMeetingView.as_view(), name="we"),
    path("ajouter/", NewWeView.as_view(), name="new_we"),
    path("<int:pk>/modifier/", WeUpdate.as_view(), name="we_update"),
    path("<int:pk>/supprimer/", WeDelete.as_view(), name="we_delete"),
]
