from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from vcm.models import Meeting
from new_vcm_meeting.forms import AddMeeting


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

    # if request.method == "POST":
    #     form = AddMeeting(request.POST)
    #     if form.is_valid():
    #         print(form.cleaned_data)
    #         return HttpResponse("La réunion a été créée avec succès.")
    # else:
    #     form = AddMeeting()
        