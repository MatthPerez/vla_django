from django.shortcuts import render
from django.views import View
from new_vcm_meeting.forms import AddMeeting


class NewVcmView(View):
    def get(self, request):
        form = AddMeeting()

        return render(request, "new_vcm_meeting/index.html", {"form": form})

    def post(self, request):
        form = AddMeeting(request.POST)
        print(form.errors)

        if form.is_valid():
            print(form)
            form.save()

            return render(
                request,
                "new_vcm_meeting/index.html",
                {"form": form},
            )

        else:
            return render(
                request,
                "new_vcm_meeting/index.html",
                {"form": form, "errors": form.errors},
            )
