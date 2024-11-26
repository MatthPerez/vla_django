from django.shortcuts import render
from django.views import View
from django.shortcuts import render
from django.views import View
from persons.models import Person
from groups.forms import AddGroup
from groups.models import Group


class GroupsView(View):
    def get(self, request):
        groups = Group.objects.all().order_by("name")
        persons = Person.objects.all()

        return render(
            request,
            "groups/index.html",
            {
                "groups": groups,
                "persons": persons,
            },
        )


class NewGroupView(View):
    def get(self, request):
        form = AddGroup()
        return render(request, "groups/new.html", {"form": form})

    def post(self, request):
        form = AddGroup(request.POST)

        if form.is_valid():
            group_data = form.cleaned_data

            group = Group(
                name=group_data["name"],
            )

            group.save()

            return render(
                request,
                "groups/new.html",
                {"form": form, "success": "Groupe ajouté avec succès !"},
            )

        else:
            print(form.errors)

            return render(
                request,
                "groups/new.html",
                {"form": form, "errors": form.errors},
            )
