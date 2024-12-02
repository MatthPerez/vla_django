from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from communication.models import Communication
from communication.forms import AddCommunication


class CommunicationView(View):
    def get(self, request):
        communications = Communication.objects.all().order_by("date")
        title = "Nouvelle communication"

        return render(
            request,
            "communication/index.html",
            {
                "communications": communications,
                "title": title,
            },
        )


class NewCommunicationView(View):
    def get(self, request):
        form = AddCommunication()
        title = "Créer une nouvelle communication"
        submit_text = "Enregistrer"

        return render(
            request,
            "communication/new.html",
            {
                "form": form,
                "title": title,
                "submit_text": submit_text,
            },
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
                {
                    "form": form,
                    "success": "Communication ajoutée avec succès.",
                },
            )

        else:
            print(form.errors)

            return render(
                request,
                "communication/new.html",
                {
                    "form": form,
                    "error": form.errors,
                },
            )


class CommunicationUpdate(View):
    def get(self, request, pk):
        communication = Communication.objects.get(pk=pk)
        submit_text = "Mettre à jour"
        title = f"Mise à jour de la communication du {communication.date}"

        form = AddCommunication(
            initial={
                "date": communication.date,
                "title": communication.title,
                "category": communication.category,
                "content1": communication.content1,
                "content2": communication.content2,
                "content3": communication.content3,
            }
        )

        return render(
            request,
            "communication/new.html",
            {
                "form": form,
                "title": title,
                "submit_text": submit_text,
            },
        )

    def post(self, request, pk):
        communication = Communication.objects.get(pk=pk)
        form = AddCommunication(request.POST)

        if form.is_valid():
            communication.date = form.cleaned_data["date"]
            communication.title = form.cleaned_data["title"]
            communication.category = form.cleaned_data["category"]
            communication.content1 = form.cleaned_data["content1"]
            communication.content2 = form.cleaned_data["content2"]
            communication.content3 = form.cleaned_data["content3"]
            communication.save()

            return redirect("communication")

        return render(
            request,
            "communication/new.html",
            {
                "form": form,
                "errors": form.errors,
            },
        )


class CommunicationDelete(View):
    def post(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        communication = get_object_or_404(Communication, pk=pk)
        communication.delete()

        return redirect("communication")
