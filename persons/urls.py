from django.urls import path
from .views import PersonsView

urlpatterns = [
    path("", PersonsView, name="persons-index"),
]
