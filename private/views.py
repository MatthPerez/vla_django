from django.shortcuts import redirect, render
from django.views import View
from persons.models import Person
from notes.models import Note
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


def is_connected(user):
    return user.is_authenticated


@method_decorator(login_required, name="dispatch")
class PrivateView(View):
    def get(self, request):
        user = request.user
        
        if is_connected(user):
            user = request.user
            person = Person.objects.get(
                firstname=user.first_name, lastname=user.last_name
            )
            persons = Person.objects.all()
            notes = Note.objects.filter(writer_id=person.id)

            context = {
                "persons": persons,
                "notes": notes,
            }

            return render(
                request,
                "private/index.html",
                context,
            )
        else:
            return redirect("signup")
