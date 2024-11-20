from django.shortcuts import render
from django.views import View
from persons.models import Person
from new_person.models import AddPerson


class NewPersonView(View):
    def get(self, request):
        form = AddPerson()
        return render(request, "new_person/index.html", {"form": form})

    def post(self, request):
        form = AddPerson(request.POST)

        if form.is_valid():
            person = form.cleaned_data

            person = Person(
                firstname=person["firstname"],
                lastname=person["lastname"],
                gender=person["gender"],
                cong_function=person["cong_function"],
                cong_status=person["cong_status"],
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
