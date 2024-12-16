from django.views.generic import ListView, DetailView
from django.views import View
from django.shortcuts import get_object_or_404, redirect, render
from vcm.models import Meeting
from vcm.forms import AddMeeting
from datetime import timedelta
from django.utils.timezone import now
from django.contrib.auth.mixins import UserPassesTestMixin


def is_admin(user):
    return user.is_authenticated and hasattr(user, "is_admin") and user.is_admin


class VcmMeetingView(ListView):
    model = Meeting.objects
    template_name = "vcm/index.html"
    context_object_name = "meetings"

    def get_queryset(self):
        three_days_ago = now().date() - timedelta(days=3)
        # in_two_month = now().date() + timedelta(days=60)

        return Meeting.objects.filter(
            date__gte=three_days_ago,
            # date__lte=in_two_month,
        ).order_by("date")


class VcmMeetingDetail(DetailView):
    model = Meeting
    template_name = "vcm/detail.html"
    context_object_name = "meeting"


class NewVcmView(UserPassesTestMixin, View):
    def test_func(self):
        return is_admin(self.request.user)

    def handle_no_permission(self):
        return redirect("vcm")
    
    def get(self, request):
        form = AddMeeting()
        big_title = "Créer une nouvelle réunion VCM"
        small_title = "Nouvelle réunion VCM"
        submit_text = "Créer nouvelle réunion"

        return render(
            request,
            "vcm/new.html",
            {
                "form": form,
                "big_title": big_title,
                "small_title": small_title,
                "submit_text": submit_text,
            },
        )

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
                {
                    "form": form,
                    "success": "Réunion ajoutée avec succès !",
                },
            )

        else:
            print(form.errors)

            return render(
                request,
                "vcm/new.html",
                {
                    "form": form,
                    "errors": form.errors,
                },
            )


class VcmUpdate(UserPassesTestMixin, View):

    def test_func(self):
        return is_admin(self.request.user)

    def handle_no_permission(self):
        return redirect("persons")

    def get(self, request, pk):
        meeting = Meeting.objects.get(pk=pk)

        big_title = f"Modifier réunion VCM du {meeting.date}"
        small_title = f"Modifier réunion du {meeting.date}"
        submit_text = "Mettre à jour la réunion"

        form = AddMeeting(
            initial={
                "date": meeting.date.strftime("%Y-%m-%d"),
                "president": meeting.president,
                "prayer1": meeting.prayer1,
                "prayer2": meeting.prayer2,
                "song1": meeting.song1,
                "song2": meeting.song2,
                "song3": meeting.song3,
                "portion": meeting.portion,
                "jewels": meeting.jewels,
                "jewels_title": meeting.jewels_title,
                "pearls": meeting.pearls,
                "reading1": meeting.reading1,
                "reading2": meeting.reading2,
                "reading3": meeting.reading3,
                "advisor2": meeting.advisor2,
                "advisor3": meeting.advisor3,
                "alloc1_type": meeting.alloc1_type,
                "alloc2_type": meeting.alloc2_type,
                "alloc3_type": meeting.alloc3_type,
                "alloc4_type": meeting.alloc4_type,
                "alloc1_duration": meeting.alloc1_duration,
                "alloc2_duration": meeting.alloc2_duration,
                "alloc4_duration": meeting.alloc4_duration,
                "alloc1pupil_hall1": meeting.alloc1pupil_hall1,
                "alloc1inter_hall1": meeting.alloc1inter_hall1,
                "alloc2pupil_hall1": meeting.alloc2pupil_hall1,
                "alloc2inter_hall1": meeting.alloc2inter_hall1,
                "alloc3pupil_hall1": meeting.alloc3pupil_hall1,
                "alloc3inter_hall1": meeting.alloc3inter_hall1,
                "alloc4pupil_hall1": meeting.alloc4pupil_hall1,
                "alloc4inter_hall1": meeting.alloc4inter_hall1,
                "alloc1pupil_hall2": meeting.alloc1pupil_hall2,
                "alloc1inter_hall2": meeting.alloc1inter_hall2,
                "alloc2pupil_hall2": meeting.alloc2pupil_hall2,
                "alloc2inter_hall2": meeting.alloc2inter_hall2,
                "alloc3pupil_hall2": meeting.alloc3pupil_hall2,
                "alloc3inter_hall2": meeting.alloc3inter_hall2,
                "alloc4pupil_hall2": meeting.alloc4pupil_hall2,
                "alloc4inter_hall2": meeting.alloc4inter_hall2,
                "pupil0_hall3": meeting.pupil0_hall3,
                "inter0_hall3": meeting.inter0_hall3,
                "pupil_hall3": meeting.pupil_hall3,
                "vcm1": meeting.vcm1,
                "vcm2": meeting.vcm2,
                "vcm3": meeting.vcm3,
                "vcm1_duration": meeting.vcm1_duration,
                "vcm2_duration": meeting.vcm2_duration,
                "vcm3_duration": meeting.vcm3_duration,
                "vcm1_title": meeting.vcm1_title,
                "vcm2_title": meeting.vcm2_title,
                "vcm3_title": meeting.vcm3_title,
                "eba": meeting.eba,
                "eba_reader": meeting.eba_reader,
                "supervisor": meeting.supervisor,
                "special_speech": meeting.special_speech,
            }
        )

        return render(
            request,
            "vcm/new.html",
            {
                "form": form,
                "big_title": big_title,
                "small_title": small_title,
                "submit_text": submit_text,
            },
        )

    def post(self, request, pk):
        meeting = Meeting.objects.get(pk=pk)
        form = AddMeeting(request.POST)
        big_title = f"Modifier réunion VCM du {meeting.date}"
        small_title = f"Modifier réunion du {meeting.date}"

        if form.is_valid():
            meeting.date = form.cleaned_data["date"]
            meeting.president = form.cleaned_data["president"]
            meeting.jewels_title = form.cleaned_data["jewels_title"]
            meeting.reading1 = form.cleaned_data["reading1"]
            meeting.reading2 = form.cleaned_data["reading2"]
            meeting.reading3 = form.cleaned_data["reading3"]
            meeting.advisor2 = form.cleaned_data["advisor2"]
            meeting.advisor3 = form.cleaned_data["advisor3"]
            meeting.alloc1_type = form.cleaned_data["alloc1_type"]
            meeting.alloc2_type = form.cleaned_data["alloc2_type"]
            meeting.alloc3_type = form.cleaned_data["alloc3_type"]
            meeting.alloc4_type = form.cleaned_data["alloc4_type"]
            meeting.alloc1_duration = form.cleaned_data["alloc1_duration"]
            meeting.alloc2_duration = form.cleaned_data["alloc2_duration"]
            meeting.alloc4_duration = form.cleaned_data["alloc4_duration"]
            meeting.alloc1pupil_hall1 = form.cleaned_data["alloc1pupil_hall1"]
            meeting.alloc1inter_hall1 = form.cleaned_data["alloc1inter_hall1"]
            meeting.alloc2pupil_hall1 = form.cleaned_data["alloc2pupil_hall1"]
            meeting.alloc2inter_hall1 = form.cleaned_data["alloc2inter_hall1"]
            meeting.alloc3pupil_hall1 = form.cleaned_data["alloc3pupil_hall1"]
            meeting.alloc3inter_hall1 = form.cleaned_data["alloc3inter_hall1"]
            meeting.alloc4pupil_hall1 = form.cleaned_data["alloc4pupil_hall1"]
            meeting.alloc4inter_hall1 = form.cleaned_data["alloc4inter_hall1"]
            meeting.alloc1pupil_hall2 = form.cleaned_data["alloc1pupil_hall2"]
            meeting.alloc1inter_hall2 = form.cleaned_data["alloc1inter_hall2"]
            meeting.alloc2pupil_hall2 = form.cleaned_data["alloc2pupil_hall2"]
            meeting.alloc2inter_hall2 = form.cleaned_data["alloc2inter_hall2"]
            meeting.alloc3pupil_hall2 = form.cleaned_data["alloc3pupil_hall2"]
            meeting.alloc3inter_hall2 = form.cleaned_data["alloc3inter_hall2"]
            meeting.alloc4pupil_hall2 = form.cleaned_data["alloc4pupil_hall2"]
            meeting.alloc4inter_hall2 = form.cleaned_data["alloc4inter_hall2"]
            meeting.pupil0_hall3 = form.cleaned_data["pupil0_hall3"]
            meeting.inter0_hall3 = form.cleaned_data["inter0_hall3"]
            meeting.pupil_hall3 = form.cleaned_data["pupil_hall3"]
            meeting.vcm1_duration = form.cleaned_data["vcm1_duration"]
            meeting.vcm2_duration = form.cleaned_data["vcm2_duration"]
            meeting.vcm3_duration = form.cleaned_data["vcm3_duration"]
            meeting.vcm1_title = form.cleaned_data["vcm1_title"]
            meeting.vcm2_title = form.cleaned_data["vcm2_title"]
            meeting.vcm3_title = form.cleaned_data["vcm3_title"]
            meeting.eba_reader = form.cleaned_data["eba_reader"]
            meeting.supervisor = form.cleaned_data["supervisor"]
            meeting.special_speech = form.cleaned_data["special_speech"]
            print("Formulaire valide, données :", form.cleaned_data)
            meeting.save()

            return redirect("vcm")
        else:
            print(form.errors)

        return render(
            request,
            "vcm/new.html",
            {
                "form": form,
                "small_title": small_title,
                "big_title": big_title,
                "errors": form.errors,
            },
        )


class VcmDelete(UserPassesTestMixin, View):

    def test_func(self):
        return is_admin(self.request.user)

    def handle_no_permission(self):
        return redirect("persons")

    def post(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        meeting = get_object_or_404(Meeting, pk=pk)
        meeting.delete()

        return redirect("vcm")
