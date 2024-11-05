from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from vcm.models import Meeting

# from persons.models import Person


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
