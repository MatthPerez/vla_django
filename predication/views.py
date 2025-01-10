from collections import defaultdict
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.views.generic import View, ListView
from predication.forms import AddPredicationMeeting
from predication.models import PredicationMeeting
import locale

locale.setlocale(locale.LC_TIME, "fr_FR.UTF-8")


def is_admin(user):
    return user.is_authenticated and hasattr(user, "is_admin") and user.is_admin


from django.views.generic import ListView
from django.utils import timezone
from predication.models import PredicationMeeting
from collections import defaultdict


class PredicationView(ListView):
    model = PredicationMeeting
    context_object_name = "groups"
    template_name = "predication/index.html"
    empty_text = "Aucune réunion trouvée."

    def get_queryset(self):
        today = timezone.now().date()
        return PredicationMeeting.objects.filter(date__gte=today).order_by("date")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = self.get_queryset()

        grouped_meetings = defaultdict(list)
        for meeting in queryset:
            grouped_meetings[meeting.date].append(meeting)

        context["groups"] = grouped_meetings.items()
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
                manager=predication_data["manager"],
                place=predication_data["place"],
                time=predication_data["time"],
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
        return redirect("predication")

    def get(self, request, pk):
        meeting = PredicationMeeting.objects.get(pk=pk)
        submit_text = "Mettre à jour la réunion"
        main_title = f"Modifier la réunion du {meeting.date}"

        form = AddPredicationMeeting(
            initial={
                "date": meeting.date,
                "manager": meeting.manager,
                "place": meeting.place,
                "time": meeting.time,
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
            meeting.manager = form.cleaned_data["manager"]
            meeting.place = form.cleaned_data["place"]
            meeting.time = form.cleaned_data["time"]
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
        return redirect("predication")

    def post(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        meeting = get_object_or_404(PredicationMeeting, pk=pk)
        meeting.delete()

        return redirect("predication")
