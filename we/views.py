from django.views.generic import ListView
from django.views import View
from django.shortcuts import get_object_or_404, redirect, render
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
            big_title = "Créer une nouvelle réunion de week-end"
            small_title = "Nouvelle réunion de week-end"
            submit_text = "Ajouter la réunion"

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
                {
                    "form": form,
                    "big_title": big_title,
                    "small_title": small_title,
                    "submit_text": submit_text,
                },
            )

        else:
            print(form.errors)

            return render(
                request,
                "we/new.html",
                {
                    "form": form,
                    "errors": form.errors,
                },
            )


class WeUpdate(View):
    def get(self, request, pk):
        meeting = WeekendMeeting.objects.get(pk=pk)
        big_title = f"Modification de la réunion du {meeting.date}"
        small_title = f"Modification de la réunion du {meeting.date}"
        submit_text = "Valider"

        form = AddWeekendMeeting(
            initial={
                "date": meeting.date,
                "president": meeting.president,
                "song1": meeting.song1,
                "song2": meeting.song2,
                "song3": meeting.song3,
                "speaker": meeting.speaker,
                "foreign_speaker": meeting.foreign_speaker,
                "speech_title": meeting.speech_title,
                "watchtower": meeting.watchtower,
                "watchtower_reader": meeting.watchtower_reader,
                "supervisor": meeting.supervisor,
                "special_speech": meeting.special_speech,
            }
        )

        return render(
            request,
            "we/new.html",
            {
                "form": form,
                "big_title": big_title,
                "small_title": small_title,
                "submit_text": submit_text,
            },
        )

    def post(self, request, pk):
        meeting = WeekendMeeting.objects.get(pk=pk)
        form = AddWeekendMeeting(request.POST)
        big_title = f"Modifier réunion VCM du {meeting.date}"
        small_title = f"Modifier réunion du {meeting.date}"
        submit_text = "Enregistrer"

        if form.is_valid():
            meeting.president = form.cleaned_data["president"]
            meeting.song1 = form.cleaned_data["song1"]
            meeting.song2 = form.cleaned_data["song2"]
            meeting.song3 = form.cleaned_data["song3"]
            meeting.speaker = form.cleaned_data["speaker"]
            meeting.foreign_speaker = form.cleaned_data["foreign_speaker"]
            meeting.speech_title = form.cleaned_data["speech_title"]
            meeting.watchtower = form.cleaned_data["watchtower"]
            meeting.watchtower_reader = form.cleaned_data["watchtower_reader"]
            meeting.supervisor = form.cleaned_data["supervisor"]
            meeting.special_speech = form.cleaned_data["special_speech"]
            meeting.save()

            return redirect("we")

        return render(
            request,
            "we/new.html",
            {
                "form": form,
                "small_title": small_title,
                "big_title": big_title,
                "submit_text": submit_text,
            },
        )


class WeDelete(View):
    def post(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        meeting = get_object_or_404(WeekendMeeting, pk=pk)
        meeting.delete()

        return redirect("we")
