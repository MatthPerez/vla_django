from django.urls import path
from .views import VcmMeetingView, NewVcmView, VcmMeetingDetail, VcmUpdate, VcmDelete

urlpatterns = [
    path("", VcmMeetingView.as_view(), name="vcm"),
    path("ajouter/", NewVcmView.as_view(), name="new_vcm"),
    path("<int:pk>/", VcmMeetingDetail.as_view(), name="vcm_detail"),
    path("<int:pk>/modifier/", VcmUpdate.as_view(), name="vcm_update"),
    path("<int:pk>/suprimer/", VcmDelete.as_view(), name="vcm_delete"),
]
