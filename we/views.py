from django.views.generic import ListView
from django.views import View
from django.shortcuts import render
from django.utils import timezone
from we.models import WeekendMeeting
from we.forms import AddWeekendMeeting


class WeMeetingView(ListView):
    model = WeekendMeeting
    template_name = "we/index.html"
    context_object_name = "meetings"

    def get_queryset(self):
        now = timezone.now()

        return WeekendMeeting.objects.filter(date__gte=now).order_by("date")


class NewWeView(View):
    def get(self, request):
        form = AddWeekendMeeting()
        return render(request, "we/new.html", {"form": form})

    def post(self, request):
        form = AddWeekendMeeting(request.POST)

        if form.is_valid():
            meeting_data = form.cleaned_data

            meeting = WeekendMeeting(
                date=meeting_data["date"],
                president=meeting_data["president"],
                song1=meeting_data["song1"],
                song2=meeting_data["song2"],
                song3=meeting_data["song3"],
                speaker=meeting_data["speaker"],
                foreign_speaker=meeting_data["foreign_speaker"],
                speech_title=meeting_data["speech_title"],
                watchtower=meeting_data.get("watchtower"),
                watchtower_reader=meeting_data.get("watchtower_reader"),
                supervisor=meeting_data.get("supervisor"),
                special_speech=meeting_data.get("special_speech"),
            )

            meeting.save()

            return render(
                request,
                "we/new.html",
                {"form": form, "success": "Réunion ajoutée avec succès!"},
            )

        else:
            print(form.errors)

            return render(
                request,
                "we/new.html",
                {"form": form, "errors": form.errors},
            )
