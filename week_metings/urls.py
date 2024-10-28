from django.urls import path
from .views import index

urlpatterns = [
    path("", index, name="week_mettings-index"),
]
