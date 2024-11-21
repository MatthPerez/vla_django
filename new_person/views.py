from django.shortcuts import render
from django.views import View
from persons.models import Person
from new_person.forms import AddPerson


class NewPersonView(View):
    def get(self, request):
        form = AddPerson()
        return render(request, "new_person/index.html", {"form": form})

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
                "new_person/index.html",
                {"form": form, "success": "Membre ajouté avec succès !"},
            )

        else:
            print(form.errors)

            return render(
                request,
                "new_person/index.html",
                {"form": form, "errors": form.errors},
            )
