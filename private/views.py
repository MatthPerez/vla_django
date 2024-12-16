from django.shortcuts import redirect, render
from django.views import View
from persons.models import Person
from notes.models import Note


def is_connected(user):
    return user.is_authenticated


class PrivateView(View):
    def get(self, request):
        persons = Person.objects.all()
        notes = Note.objects.all()

        return render(
            request,
            "private/index.html",
            {
                "persons": persons,
                "notes": notes,
            },
        )


