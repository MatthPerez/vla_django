from django.shortcuts import render
from django.views import View


class WeView(View):
    def get(self, request):
        return render(
            request,
            "we/index.html",
        )
