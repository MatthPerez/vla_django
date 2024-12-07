from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.shortcuts import render
from django.views import View
from publications.forms import AddPublication
from publications.models import Publication


class PublicationView(View):
    def get(self, request):
        publications = Publication.objects.order_by("name")

        return render(
            request,
            "publications/index.html",
            {
                "publications": publications,
            },
        )


class NewPublicationView(View):
    def get(self, request):
        form = AddPublication()
        title = "Créer une nouvelle publication"
        submit_text = "Créer"

        return render(
            request,
            "publications/new.html",
            {
                "form": form,
                "title": title,
                "submit_text": submit_text,
            },
        )

    def post(self, request):
        form = AddPublication(request.POST)

        if form.is_valid():
            group_data = form.cleaned_data

            group = Publication(
                name=group_data["name"],
            )

            group.save()

            return render(
                request,
                "publications/new.html",
                {
                    "form": form,
                    "success": "Publication ajoutée avec succès !",
                },
            )

        else:
            print(form.errors)

            return render(
                request,
                "publications/new.html",
                {
                    "form": form,
                    "errors": form.errors,
                },
            )


class PublicationUpdate(View):
    def get(self, request, pk):
        publication = Publication.objects.get(pk=pk)
        title = "Modifier la publication"
        submit_text = "Enregistrer"

        form = AddPublication(
            initial={
                "name": publication.name,
            }
        )

        return render(
            request,
            "publications/new.html",
            {
                "form": form,
                "title": title,
                "submit_text": submit_text,
            },
        )

    def post(self, request, pk):
        publication = Publication.objects.get(pk=pk)
        form = AddPublication(request.POST)

        if form.is_valid():
            publication.name = form.cleaned_data["name"]
            publication.save()

        return redirect("publications")


class PublicationDelete(View):
    def post(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        publication = get_object_or_404(Publication, pk=pk)
        publication.delete()
        
        return redirect("publications")
