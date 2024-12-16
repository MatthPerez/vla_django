from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import View, ListView
from predication.models import PredicationMeeting
from predication.forms import AddPredicationMeeting
from datetime import datetime
import locale
from django.contrib.auth.mixins import UserPassesTestMixin

locale.setlocale(locale.LC_TIME, "fr_FR.UTF-8")


def is_admin(user):
    return user.is_authenticated and hasattr(user, "is_admin") and user.is_admin


class PredicationView(ListView):
    model = PredicationMeeting
    context_object_name = "meetings"
    template_name = "predication/index.html"
    empty_text = "Aucune réunion trouvée."

    def get_queryset(self):
        today = datetime.today().date()
        return PredicationMeeting.objects.filter(date__gte=today).order_by("date")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = self.get_queryset()

        context["count"] = queryset.count()
        context["empty_text"] = self.empty_text
        return context


class NewPredicationView(UserPassesTestMixin, View):

    def test_func(self):
        return is_admin(self.request.user)

    def handle_no_permission(self):
        return redirect("predication")

    def get(self, request):
        form = AddPredicationMeeting()
        submit_text = "Ajouter la réunion"
        main_title = "Nouvelle réunion pour la prédication"

        return render(
            request,
            "predication/new.html",
            {
                "form": form,
                "submit_text": submit_text,
                "main_title": main_title,
            },
        )

    def post(self, request):
        form = AddPredicationMeeting(request.POST)
        submit_text = "Ajouter la réunion"

        if form.is_valid():
            predication_data = form.cleaned_data

            predication_meeting = PredicationMeeting(
                date=predication_data["date"],
                manager1=predication_data["manager1"],
                place1=predication_data["place1"],
                time1=predication_data["time1"],
                manager2=predication_data["manager2"],
                place2=predication_data["place2"],
                time2=predication_data["time2"],
                manager3=predication_data["manager3"],
                place3=predication_data["place3"],
                time3=predication_data["time3"],
            )

            predication_meeting.save()

            return render(
                request,
                "predication/new.html",
                {
                    "form": form,
                    "submit_text": submit_text,
                    "success": "La réunion a été ajouté avec succès.",
                },
            )

        else:
            print(form.errors)

            return render(
                request,
                "predication/new.html",
                {
                    "form": form,
                    "errors": form.errors,
                },
            )


class PredicationMeetingUpdate(UserPassesTestMixin, View):

    def test_func(self):
        return is_admin(self.request.user)

    def handle_no_permission(self):
        return redirect("persons")

    def get(self, request, pk):
        meeting = PredicationMeeting.objects.get(pk=pk)
        submit_text = "Mettre à jour la réunion"
        main_title = f"Modifier la réunion du {meeting.date}"

        form = AddPredicationMeeting(
            initial={
                "date": meeting.date,
                "manager1": meeting.manager1,
                "manager2": meeting.manager2,
                "manager3": meeting.manager3,
                "place1": meeting.place1,
                "place2": meeting.place2,
                "place3": meeting.place3,
                "time1": meeting.time1,
                "time2": meeting.time2,
                "time3": meeting.time3,
            }
        )

        return render(
            request,
            "predication/new.html",
            {
                "form": form,
                "submit_text": submit_text,
                "main_title": main_title,
            },
        )

    def post(self, request, pk):
        meeting = PredicationMeeting.objects.get(pk=pk)
        form = AddPredicationMeeting(request.POST)

        if form.is_valid():
            meeting.date = form.cleaned_data["date"]
            meeting.manager1 = form.cleaned_data["manager1"]
            meeting.manager2 = form.cleaned_data["manager2"]
            meeting.manager3 = form.cleaned_data["manager3"]
            meeting.place1 = form.cleaned_data["place1"]
            meeting.place2 = form.cleaned_data["place2"]
            meeting.place3 = form.cleaned_data["place3"]
            meeting.time1 = form.cleaned_data["time1"]
            meeting.time2 = form.cleaned_data["time2"]
            meeting.time3 = form.cleaned_data["time3"]
            meeting.save()

            return redirect("predication")

        return render(
            request,
            "predication/new.html",
            {
                "form": form,
                "errors": form.errors,
            },
        )


class PredicationDelete(UserPassesTestMixin, View):

    def test_func(self):
        return is_admin(self.request.user)

    def handle_no_permission(self):
        return redirect("persons")

    def post(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        meeting = get_object_or_404(PredicationMeeting, pk=pk)
        meeting.delete()

        return redirect("predication")
