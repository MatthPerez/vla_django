from django.urls import path
from .views import PersonsView, PersonCreate

urlpatterns = [
    path("", PersonsView.as_view(), name="persons"),
    path("ajouter/", PersonCreate.as_view(), name="new_person"),
]
