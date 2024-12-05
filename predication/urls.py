from django.urls import path
from .views import PredicationView

urlpatterns = [
    path("", PredicationView.as_view(), name="predication"),
]
