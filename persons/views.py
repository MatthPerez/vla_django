from django.views import View
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404, redirect, render
# from django.contrib.auth.decorators import login_required
from .models import Person
from .forms import AddPerson


class PersonsView(ListView):
    model = Person
    context_object_name = "persons"
    template_name = "persons/index.html"
    empty_text = "Aucun membre trouvé."
    ordering = ["lastname", "firstname"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["count"] = self.get_queryset().count()
        context["empty_text"] = self.empty_text
        return context


class PersonDetail(DetailView):
    model = Person
    context_object_name = "person"
    template_name = "persons/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["role_display_list"] = self.object.get_roles_display()
        return context


# @login_required
class PersonCreate(View):
    def get(self, request):
        form = AddPerson()
        submit_text = "Créer"
        title = "Créer un nouveau membre"

        return render(
            request,
            "persons/new.html",
            {
                "form": form,
                "title": title,
                "submit_text": submit_text,
            },
        )

    def post(self, request):
        form = AddPerson(request.POST)

        if form.is_valid():
            person_data = form.cleaned_data

            person = Person(
                firstname=person_data["firstname"],
                lastname=person_data["lastname"],
                gender=person_data["gender"],
                cong_function=person_data["cong_function"],
                cong_status=person_data["cong_status"],
                cong_roles=",".join(person_data["cong_roles"]),
                group=person_data["group"],
            )
            person.save()

            return render(
                request,
                "persons/new.html",
                {"form": AddPerson(), "success": "Membre ajouté avec succès."},
            )
        else:
            return render(
                request,
                "persons/new.html",
                {"form": form, "errors": form.errors},
            )


# @login_required
class PersonUpdate(View):
    def get(self, request, pk):
        person = Person.objects.get(pk=pk)
        submit_text = "Mettre à jour"
        title = f"Mise à jour de {person.firstname} {person.lastname}"

        form = AddPerson(
            initial={
                "firstname": person.firstname,
                "lastname": person.lastname,
                "gender": person.gender,
                "cong_function": person.cong_function,
                "cong_roles": person.cong_roles.split(","),
                "cong_status": person.cong_status,
                "group": person.group,
            }
        )

        return render(
            request,
            "persons/new.html",
            {
                "form": form,
                "title": title,
                "submit_text": submit_text,
            },
        )

    def post(self, request, pk):
        person = Person.objects.get(pk=pk)
        form = AddPerson(request.POST)

        if form.is_valid():
            person.firstname = form.cleaned_data["firstname"]
            person.lastname = form.cleaned_data["lastname"]
            person.gender = form.cleaned_data["gender"]
            person.cong_function = form.cleaned_data["cong_function"]
            person.cong_roles = form.cleaned_data["cong_roles"]
            person.cong_status = form.cleaned_data["cong_status"]
            person.group = form.cleaned_data["group"]
            person.save()

            return redirect("persons")

        return render(
            request,
            "persons/new.html",
            {
                "form": form,
                "errors": form.errors,
            },
        )


# @login_required
class PersonDelete(View):
    def post(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        person = get_object_or_404(Person, pk=pk)
        person.delete()

        return redirect("persons")
