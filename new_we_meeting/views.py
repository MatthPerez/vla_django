from django.shortcuts import render
from django.views import View
from new_we_meeting.forms import AddWeekendMeeting
from we.models import WeekendMeeting


class NewWeView(View):
    def get(self, request):
        form = AddWeekendMeeting()
        return render(request, "new_we_meeting/index.html", {"form": form})

    def post(self, request):
        form = AddWeekendMeeting(request.POST)

        if form.is_valid():
            meeting_data = form.cleaned_data

            meeting = WeekendMeeting(
                date=meeting_data["date"],
                president=meeting_data["president"],
                prayer1=meeting_data["prayer1"],
                prayer2=meeting_data["prayer2"],
                song1=meeting_data["song1"],
                song2=meeting_data["song2"],
                song3=meeting_data["song3"],
                watchtower=meeting_data.get("watchtower"),
                watchtower_reader=meeting_data.get("watchtower_reader"),
                supervisor=meeting_data.get("supervisor"),
                special_speech=meeting_data.get("special_speech"),
            )

            meeting.save()

            return render(
                request,
                "new_we_meeting/index.html",
                {"form": form, "success": "Réunion ajoutée avec succès!"},
            )

        else:
            print(form.errors)

            return render(
                request,
                "new_we_meeting/index.html",
                {"form": form, "errors": form.errors},
            )
