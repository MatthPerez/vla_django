from django.shortcuts import redirect, render, get_object_or_404
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
        big_title = "Créer un nouveau groupe"
        small_title = "Nouveau groupe"
        submit_text = "Créer le groupe"

        context = {
            "big_title": big_title,
            "small_title": small_title,
            "submit_text": submit_text,
            "form": form,
        }

        return render(
            request,
            "groups/new.html",
            context,
        )

    def post(self, request):
        form = AddGroup(request.POST)

        if form.is_valid():
            group_data = form.cleaned_data

            group = Group(
                name=group_data["name"],
            )

            group.save()

            context = {
                "form": form,
                "success": "Groupe ajouté avec succès !",
            }

            return render(
                request,
                "groups/index.html",
                context,
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


class GroupUpdate(UserPassesTestMixin, View):
    def test_func(self):
        return is_admin(self.request.user)

    def handle_no_permission(self):
        return redirect("groups")

    def get(self, request, pk):
        group = Group.objects.get(pk=pk)
        title = f"Mise à jour du groupe {group.name}"
        submit_text = "Enregistrer"

        form = AddGroup(
            initial={
                "name": group.name,
            }
        )

        context = {
            "title": title,
            "submit_text": submit_text,
            "form": form,
        }

        return render(
            request,
            "groups/new.html",
            context,
        )

    def post(welf, request, pk):
        group = Group.objects.get(pk=pk)
        form = AddGroup(request.POST)

        if form.is_valid():
            group.name = (form.cleaned_data["name"],)
            group.save()

            return redirect("groups")

        context = {
            "form": form,
            "errors": form.errors,
        }

        return render(
            request,
            "groups/new.html",
            context,
        )


class GroupDelete(UserPassesTestMixin, View):
    def test_func(self):
        return is_admin(self.request.user)

    def handle_no_permission(self):
        return redirect("groups")

    def post(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        group = get_object_or_404(Group, pk=pk)
        group.delete()

        return redirect("groups")
