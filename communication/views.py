from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from communication.models import Communication
from communication.forms import AddCommunication
from django.contrib.auth.mixins import UserPassesTestMixin


def is_admin(user):
    return user.is_authenticated and hasattr(user, "is_admin") and user.is_admin


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

            return redirect("communication")

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


class CommunicationUpdate(UserPassesTestMixin, View):

    def test_func(self):
        return is_admin(self.request.user)

    def handle_no_permission(self):
        return redirect("communication")

    def get(self, request, pk):
        communication = Communication.objects.get(pk=pk)
        submit_text = "Mettre à jour"
        title = f"Mise à jour de la communication du {communication.date}"

        form = AddCommunication(
            initial={
                "date": communication.date.strftime("%Y-%m-%d"),
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

        else:
            print(form.errors)

            return redirect("communication")


class CommunicationDelete(UserPassesTestMixin, View):

    def test_func(self):
        return is_admin(self.request.user)

    def handle_no_permission(self):
        return redirect("communication")

    def post(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        communication = get_object_or_404(Communication, pk=pk)
        communication.delete()

        return redirect("communication")
