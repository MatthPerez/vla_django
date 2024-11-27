from django.shortcuts import render
from django.views import View
from communication.models import Communication
from communication.forms import AddCommunication


class CommunicationView(View):
    def get(self, request):
        communications = Communication.objects.all().order_by("date")

        return render(
            request,
            "communication/index.html",
            {"communications": communications},
        )


class NewCommunicationView(View):
    def get(self, request):
        form = AddCommunication()

        return render(
            request,
            "communication/new.html",
            {"form": form},
        )

    def post(self, request):
        form = AddCommunication(request.POST)

        if form.is_valid():
            comm_data = form.cleaned_data

            comm = Communication(
                date=comm_data["date"],
                title=comm_data["title"],
                category=comm_data["category"],
                content1=comm_data["content1"],
                content2=comm_data["content2"],
                content3=comm_data["content3"],
            )

            comm.save()

            return render(
                request,
                "communication/new.html",
                {"form": form, "success": "Communication ajoutée avec succès."},
            )

        else:
            print(form.errors)

            return render(
                request,
                "communication/new.html",
                {"form": form, "error": form.errors},
            )
