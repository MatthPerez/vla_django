from django.urls import path
from .views import PersonsView, PersonCreate, PersonDetail, PersonUpdate, PersonDelete

urlpatterns = [
    path("", PersonsView.as_view(), name="persons"),
    path("ajouter/", PersonCreate.as_view(), name="person_add"),
    path("<int:pk>/", PersonDetail.as_view(), name="person_detail"),
    path("<int:pk>/modifier/", PersonUpdate.as_view(), name="person_update"),
    path("<int:pk>/supprimer/", PersonDelete.as_view(), name="person_delete"),
]
