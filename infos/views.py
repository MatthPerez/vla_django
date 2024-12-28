from django.shortcuts import render
from django.views import View


class InfosView(View):
    def get(self, request):
        return render(
            request,
            "infos/index.html",
        )
