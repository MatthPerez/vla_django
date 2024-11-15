from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from new_vcm_meeting.forms import AddMeeting
from vcm.models import Meeting
from django.utils import timezone


class VcmView(View):
    def get(self, request):
        return render(
            self,
            request,
            "vcm/index.html",
        )


class VcmMeetingView(ListView):
    model = Meeting
    template_name = "vcm/index.html"
    context_object_name = "meetings"

    def get_queryset(self):
        now = timezone.now()

        return Meeting.objects.filter(date__gte=now)

    def post(self, request):
        form = AddMeeting(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("La réunion a été créée avec succès.")
        return render(request, "vcm/index.html", {"form": form})
