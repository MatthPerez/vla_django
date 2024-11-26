from django.shortcuts import render
from django.views import View


class CommunicationView(View):
    def get(self, request):
        return render(
            request,
            "communication/index.html",
        )


class NewCommunicationView(View):
    def get(self, request):
        return render(
            request,
            "communication/new.html",
        )
