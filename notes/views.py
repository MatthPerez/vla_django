from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.contrib.auth.mixins import UserPassesTestMixin
from persons.models import Person
from accounts.models import CustomUser
from .models import Note
from .forms import AddNote


def is_connected(user):
    return user.is_authenticated


from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import UserPassesTestMixin


class NewNote(UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_authenticated

    def handle_no_permission(self):
        return redirect("index")

    def get(self, request):
        form = AddNote()
        title = "Créer une nouvelle note"
        submit_text = "Enregistrer"

        return render(
            request,
            "notes/new.html",
            {
                "form": form,
                "title": title,
                "submit_text": submit_text,
            },
        )

    def post(self, request):
        form = AddNote(request.POST)

        if form.is_valid():
            note_data = form.cleaned_data

            user = CustomUser.objects.get(id=request.user.id)

            person = Person.objects.filter(firstname=user.first_name).first()

            if person:
                note = Note(
                    title=note_data["title"],
                    content=note_data["content"],
                    link=note_data["link"],
                    writer_id=person.id,
                )
                note.save()

            return render(
                request,
                "notes/new.html",
                {
                    "form": form,
                    "success": "Note ajoutée avec succès !",
                },
            )

        else:
            print(form.errors)

            return render(
                request,
                "notes/new.html",
                {
                    "form": form,
                    "errors": form.errors,
                },
            )


class NoteUpdate(UserPassesTestMixin, View):
    def test_func(self):
        return is_connected(self.request.user)

    def handle_no_permission(self):
        return redirect("index")

    def get(self, request, pk):
        note = Note.objects.get(pk=pk)
        submit_text = "Mettre à jour"
        title = f"Mise à jour de la note : {note.title}"

        form = AddNote(
            initial={
                "title": note.title,
                "content": note.content,
                "link": note.link,
            }
        )

        return render(
            request,
            "notes/new.html",
            {
                "form": form,
                "title": title,
                "submit_text": submit_text,
            },
        )

    def post(self, request, pk):
        note = Note.objects.get(pk=pk)
        form = AddNote(request.POST)

        if form.is_valid():
            note.title = form.cleaned_data["title"]
            note.content = form.cleaned_data["content"]
            note.link = form.cleaned_data["link"]
            note.save()

            return redirect("private")

        else:
            print(form.errors)

            return redirect("private")


class NoteDelete(UserPassesTestMixin, View):
    def test_func(self):
        return is_connected(self.request.user)

    def handle_no_permission(self):
        return redirect("index")

    def post(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        note = get_object_or_404(Note, pk=pk)
        note.delete()

        return redirect("private")
