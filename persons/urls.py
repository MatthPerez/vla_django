from django.urls import path
from .views import PersonsView, NewPersonView

urlpatterns = [
    path("", PersonsView.as_view(), name="persons"),
    path("ajouter/", NewPersonView.as_view(), name="new_person"),
]
