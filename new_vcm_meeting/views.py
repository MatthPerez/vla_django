from django.shortcuts import render
from django.views import View
from new_vcm_meeting.forms import AddMeeting


# class NewVcmView(View):
#     def weekMeetingForm(request):
#         form = AddMeeting()

#         return render(
#             request,
#             "new_vcm_meeting/index.html",
#             {"form": form},
#         )

class NewVcmView(View):
    def get(self, request):
        return render(
            request,
            "new_vcm_meeting/index.html",
        )