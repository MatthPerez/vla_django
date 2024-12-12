from django.urls import path
from .views import register

urlpatterns = [
    path("inscription/", register, name="register"),
]
