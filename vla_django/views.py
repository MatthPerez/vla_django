from django.shortcuts import render
from django.views import View
from new_vcm_meeting.forms import AddMeeting


class HomeView(View):
    def get(self, request):
        return render(
            request,
            "vla_django/index.html",
        )

    def week_meeting_form(request):
        form = AddMeeting()

        return render(request, "new_vcm_meeting/index.html", {"form": form})
