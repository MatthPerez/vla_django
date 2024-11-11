from django.shortcuts import render
from django.views import View


class NewVcmView(View):
    def get(self, request):
        return render(
            request,
            "new_vcm_meeting/index.html",
        )
