from django.urls import path
from .views import VcmView

urlpatterns = [
    path("", VcmView, name="vcm-index"),
]
