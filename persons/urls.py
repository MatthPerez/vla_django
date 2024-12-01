from django.urls import path
from .views import PersonsView

urlpatterns = [
    path("", PersonsView.as_view(), name="persons"),
]
