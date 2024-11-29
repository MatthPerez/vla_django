from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView
from django.shortcuts import render
from django.views import View
from persons.models import Person
from persons.forms import AddPerson


class PersonsView(ListView):
    model = Person
    context_object_name = "persons"
    template_name = "persons/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["count"] = self.get_queryset().count()
        return context


class PersonDetail(DetailView):
    model = Person
    context_object_name = "person"
    template_name = "persons/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["role_display_list"] = self.object.get_roles_display()
        return context


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


class PersonUpdate(View):
    def get(self, request, pk):
        person = Person.objects.get(pk=pk)
        form = AddPerson(instance=person)
        submit_text = "Mettre à jour"
        title = f"Mise à jour de {person.firstname} {person.lastname}"

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
        form = AddPerson(request.POST, instance=person)

        if form.is_valid():
            form.save()
            return render(
                request,
                "persons/new.html",
                {
                    "form": form,
                    "success": "Membre mis à jour avec succès.",
                },
            )

        else:
            print(form.errors)
            return render(
                request,
                "persons/new.html",
                {
                    "form": form,
                    "errors": form.errors,
                },
            )
