from django.shortcuts import redirect, render
from django.views import View
from persons.models import Person
from groups.models import Group
from groups.forms import AddGroup
from django.contrib.auth.mixins import UserPassesTestMixin


def is_admin(user):
    return user.is_authenticated and hasattr(user, "is_admin") and user.is_admin


class GroupsView(View):
    def get(self, request):
        groups = Group.objects.order_by("name")
        persons = Person.objects.all()

        return render(
            request,
            "groups/index.html",
            {
                "groups": groups,
                "persons": persons,
            },
        )


class NewGroupView(UserPassesTestMixin, View):

    def test_func(self):
        return is_admin(self.request.user)

    def handle_no_permission(self):
        return redirect("groups")

    def get(self, request):
        form = AddGroup()

        return render(
            request,
            "groups/new.html",
            {
                "form": form,
            },
        )

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
                {
                    "form": form,
                    "success": "Groupe ajouté avec succès !",
                },
            )

        else:
            print(form.errors)

            return render(
                request,
                "groups/new.html",
                {
                    "form": form,
                    "errors": form.errors,
                },
            )
