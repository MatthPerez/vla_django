from django.views.generic import ListView, DetailView
from django.views import View
from django.shortcuts import render
from vcm.models import Meeting
from vcm.forms import AddMeeting
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


class NewVcmView(View):
    def get(self, request):
        form = AddMeeting()
        return render(request, "vcm/new.html", {"form": form})

    def post(self, request):
        form = AddMeeting(request.POST)

        if form.is_valid():
            meeting_data = form.cleaned_data

            meeting = Meeting(
                date=meeting_data["date"],
                president=meeting_data["president"],
                prayer1=meeting_data["prayer1"],
                prayer2=meeting_data["prayer2"],
                song1=meeting_data["song1"],
                song2=meeting_data["song2"],
                song3=meeting_data["song3"],
                portion=meeting_data["portion"],
                jewels=meeting_data["jewels"],
                jewels_title=meeting_data["jewels_title"],
                pearls=meeting_data["pearls"],
                reading1=meeting_data["reading1"],
                reading2=meeting_data.get("reading2"),
                reading3=meeting_data.get("reading3"),
                advisor2=meeting_data.get("advisor2"),
                advisor3=meeting_data.get("advisor3"),
                alloc1_type=meeting_data["alloc1_type"],
                alloc2_type=meeting_data["alloc2_type"],
                alloc3_type=meeting_data.get("alloc3_type"),
                alloc4_type=meeting_data.get("alloc4_type"),
                alloc1_duration=meeting_data["alloc1_duration"],
                alloc2_duration=meeting_data["alloc2_duration"],
                alloc3_duration=meeting_data.get("alloc3_duration"),
                alloc4_duration=meeting_data.get("alloc4_duration"),
                alloc1pupil_hall1=meeting_data.get("alloc1pupil_hall1"),
                alloc1inter_hall1=meeting_data.get("alloc1inter_hall1"),
                alloc2pupil_hall1=meeting_data.get("alloc2pupil_hall1"),
                alloc2inter_hall1=meeting_data.get("alloc2inter_hall1"),
                alloc3pupil_hall1=meeting_data.get("alloc3pupil_hall1"),
                alloc3inter_hall1=meeting_data.get("alloc3inter_hall1"),
                alloc4pupil_hall1=meeting_data.get("alloc4pupil_hall1"),
                alloc4inter_hall1=meeting_data.get("alloc4inter_hall1"),
                alloc1pupil_hall2=meeting_data.get("alloc1pupil_hall2"),
                alloc1inter_hall2=meeting_data.get("alloc1inter_hall2"),
                alloc2pupil_hall2=meeting_data.get("alloc2pupil_hall2"),
                alloc2inter_hall2=meeting_data.get("alloc2inter_hall2"),
                alloc3pupil_hall2=meeting_data.get("alloc3pupil_hall2"),
                alloc3inter_hall2=meeting_data.get("alloc3inter_hall2"),
                alloc4pupil_hall2=meeting_data.get("alloc4pupil_hall2"),
                alloc4inter_hall2=meeting_data.get("alloc4inter_hall2"),
                pupil0_hall3=meeting_data.get("pupil0_hall3"),
                inter0_hall3=meeting_data.get("inter0_hall3"),
                pupil_hall3=meeting_data.get("pupil_hall3"),
                vcm1=meeting_data["vcm1"],
                vcm2=meeting_data.get("vcm2"),
                vcm3=meeting_data.get("vcm3"),
                vcm1_duration=meeting_data["vcm1_duration"],
                vcm2_duration=meeting_data.get("vcm2_duration"),
                vcm3_duration=meeting_data.get("vcm3_duration"),
                vcm1_title=meeting_data["vcm1_title"],
                vcm2_title=meeting_data.get("vcm2_title"),
                vcm3_title=meeting_data.get("vcm3_title"),
                eba=meeting_data.get("eba"),
                eba_reader=meeting_data.get("eba_reader"),
                supervisor=meeting_data.get("supervisor"),
                special_speech=meeting_data.get("special_speech"),
            )

            meeting.save()

            return render(
                request,
                "vcm/new.html",
                {"form": form, "success": "Réunion ajoutée avec succès !"},
            )

        else:
            print(form.errors)

            return render(
                request,
                "vcm/new.html",
                {"form": form, "errors": form.errors},
            )
