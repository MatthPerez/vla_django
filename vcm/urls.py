from django.urls import path
from .views import VcmMeetingView

urlpatterns = [
    path("", VcmMeetingView, name="vcm-index"),    
]
