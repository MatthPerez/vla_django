from django.views.generic import ListView, DetailView
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


class PersonsDetail(DetailView):
    model = Person
    context_object_name = "persons"
    template_name = "persons/detail.html"


class NewPersonView(View):
    def get(self, request):
        form = AddPerson()
        return render(request, "persons/new.html", {"form": form})

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
                {"form": form, "success": "Membre ajouté avec succès !"},
            )

        else:
            print(form.errors)

            return render(
                request,
                "persons/new.html",
                {"form": form, "errors": form.errors},
            )
