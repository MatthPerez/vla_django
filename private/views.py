from django.shortcuts import redirect, render
from django.views import View
from persons.models import Person
from notes.models import Note


def is_connected(user):
    return user.is_authenticated


class PrivateView(View):
    def get(self, request):
        user = request.user
        person = Person.objects.get(firstname=user.first_name, lastname=user.last_name)
        persons = Person.objects.all()
        notes = Note.objects.filter(writer_id=person.id)

        return render(
            request,
            "private/index.html",
            {
                "persons": persons,
                "notes": notes,
            },
        )
