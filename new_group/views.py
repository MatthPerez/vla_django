from django.shortcuts import render
from django.views import View
from new_group.forms import AddGroup
from groups.models import Group


class NewGroupView(View):
    def get(self, request):
        form = AddGroup()
        return render(request, "new_group/index.html", {"form": form})

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
                "new_group/index.html",
                {"form": form, "success": "Groupe ajouté avec succès !"},
            )

        else:
            print(form.errors)

            return render(
                request,
                "new_group/index.html",
                {"form": form, "errors": form.errors},
            )
