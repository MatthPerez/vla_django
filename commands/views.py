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
        commands_by_persons = Command.objects.order_by("person_id")
        commands_by_publications = Command.objects.order_by("publication_id")

        return render(
            request,
            "commands/index.html",
            {
                "publications": publications,
                "persons": persons,
                "commands_by_persons": commands_by_persons,
                "commands_by_publications": commands_by_publications,
            },
        )


class NewCommandView(View):
    def get(self, request):
        form = AddCommand()
        big_title = "Créer une nouvelle commande"
        small_title = "Nouvelle commande"
        submit_text = "Créer nouvelle commande"

        return render(
            request,
            "commands/new.html",
            {
                "form": form,
                "big_title": big_title,
                "small_title": small_title,
                "submit_text": submit_text,
            },
        )

    def post(self, request):
        form = AddCommand(request.POST)
        big_title = "Créer une nouvelle commande de publication"
        small_title = "Nouvelle commande de publication"

        if form.is_valid():
            command_data = form.cleaned_data

            Command.objects.create(
                person=command_data["person"],
                publication=command_data["publication"],
                quantity=command_data["quantity"],
            )

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


class CommandUpdate(View):
    def get(self, request, pk):
        command = get_object_or_404(Command, pk=pk)

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
                "quantity": command.quantity,
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

    def post(self, request, pk):
        command = get_object_or_404(Command, pk=pk)
        form = AddCommand(request.POST)

        if form.is_valid():
            command.person = form.cleaned_data["person"]
            command.publication = form.cleaned_data["publication"]
            command.quantity = form.cleaned_data["quantity"]
            command.save()

            success_message = "La commande a été mise à jour avec succès."
            
            return redirect("commands")

            # return render(
            #     request,
            #     "commands/new.html",
            #     {
            #         "form": form,
            #         "big_title": f"Modifier la commande de {command.person.fullname}",
            #         "small_title": f"Publication actuelle : {command.publication.name}",
            #         "submit_text": "Enregistrer",
            #         "success": success_message,
            #     },
            # )
        else:
            return render(
                request,
                "commands/new.html",
                {
                    "form": form,
                    "big_title": f"Modifier la commande de {command.person.fullname}",
                    "small_title": f"Publication actuelle : {command.publication.name}",
                    "submit_text": "Enregistrer",
                    "errors": form.errors,
                },
            )


class CommandDelete(View):
    def post(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        command = get_object_or_404(Command, pk=pk)
        command.delete()

        return redirect("commands")
