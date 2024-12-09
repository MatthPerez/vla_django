from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.shortcuts import render
from django.views import View
from commands.forms import AddCommand
from publications.models import Publication
from persons.models import Person


class CommandsView(View):
    def get(self, request):
        publications = Publication.objects.order_by("name")
        persons = Person.objects.order_by("group", "lastname", "firstname")

        return render(
            request,
            "commands/index.html",
            {
                "publications": publications,
                "persons": persons,
            },
        )


class NewCommandView(View):
    def get(self, request):
        form = AddCommand()
        title = "Créer une nouvelle commande"
        submit_text = "Créer la commande"

        return render(
            request,
            "commands/new.html",
            {
                "form": form,
                "title": title,
                "submit_text": submit_text,
            },
        )

    def post(self, request):
        form = AddCommand(request.POST)

        if form.is_valid():
            group_data = form.cleaned_data

            group = Publication(
                publication=group_data["publication"],
                person=group_data["person"],
            )

            group.save()

            return render(
                request,
                "commands/new.html",
                {
                    "form": form,
                    "success": "Commande ajoutée avec succès !",
                },
            )

        else:
            print(form.errors)

            return render(
                request,
                "commands/new.html",
                {
                    "form": form,
                    "errors": form.errors,
                },
            )


class CommandUpdate(View):
    def get(self, request, pk):
        publication = Publication.objects.get(pk=pk)
        title = "Modifier la commande"
        submit_text = "Enregistrer"

        form = AddCommand(
            initial={
                "name": publication.name,
            }
        )

        return render(
            request,
            "commands/new.html",
            {
                "form": form,
                "title": title,
                "submit_text": submit_text,
            },
        )

    def post(self, request, pk):
        publication = Publication.objects.get(pk=pk)
        form = AddCommand(request.POST)

        if form.is_valid():
            publication.name = form.cleaned_data["name"]
            publication.save()

        return redirect("commands")


class CommandDelete(View):
    def post(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        publication = get_object_or_404(Publication, pk=pk)
        publication.delete()

        return redirect("commands")
