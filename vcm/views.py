from django.http import Http404
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from vcm.models import Meeting
from datetime import datetime


class VcmMeetingView(ListView):
    model = Meeting
    template_name = "vcm/index.html"
    context_object_name = "meetings"

    def get_queryset(self):
        today = datetime.today().date()
        return Meeting.objects.filter(date__gte=today).order_by("date")


class VcmMeetingDetail(DetailView):
    model = Meeting
    template_name = "vcm/detail.html"
    context_object_name = "meeting"