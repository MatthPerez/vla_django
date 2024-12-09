from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.shortcuts import render
from django.views import View
from commands.forms import AddCommand
from publications.models import Publication
from persons.models import Person
from commands.models import Command


class CommandsView(View):
    def get(self, request):
        publications = Publication.objects.order_by("name")
        persons = Person.objects.order_by("group", "lastname", "firstname")
        commands = Command.objects.order_by("person_id")

        return render(
            request,
            "commands/index.html",
            {
                "publications": publications,
                "persons": persons,
                "commands": commands,
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
        big_title = "Créer une nouvelle commande de publication"
        small_title = "Nouvelle commande de publication"

        if form.is_valid():
            command_data = form.cleaned_data

            command = Command.objects.create(
                person=command_data["person"],
                publication=command_data["publication"],
            )

            command.save()

            return render(
                request,
                "commands/new.html",
                {
                    "form": form,
                    "success": "Commande ajoutée avec succès !",
                    "big_title": big_title,
                    "small_title": small_title,
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


from django.shortcuts import get_object_or_404, render
from django.views import View
from commands.models import Command


from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Command
from .forms import AddCommand  # Si c'est AddCommand que vous utilisez


class CommandUpdate(View):
    def get(self, request, pk):
        # Récupérer la commande par son identifiant
        command = get_object_or_404(Command, pk=pk)

        # Extraire les données liées à la personne et à la publication
        my_person = command.person.fullname if command.person else "Personne inconnue"
        my_publication = (
            command.publication.name if command.publication else "Publication inconnue"
        )

        big_title = f"Modifier la commande de {my_person}"
        small_title = f"Publication actuelle : {my_publication}"
        submit_text = "Enregistrer"

        form = AddCommand(
            initial={
                "person": command.person,
                "publication": command.publication,
            }
        )

        return render(
            request,
            "commands/new.html",
            {
                "big_title": big_title,
                "small_title": small_title,
                "submit_text": submit_text,
                "form": form,
            },
        )


class CommandDelete(View):
    def post(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        command = get_object_or_404(Command, pk=pk)
        command.delete()

        return redirect("commands")
