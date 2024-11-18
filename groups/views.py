from django.shortcuts import render
from django.views import View
from persons.models import Person


class GroupsView(View):
    def get(self, request):
        groups = (
            Person.objects.exclude(group__isnull=True)
            .exclude(group="")
            .values_list("group", flat=True)
            .distinct()
        )
        persons = Person.objects.all().order_by("lastname", "firstname")
        
        for person in persons:
            if "Responsable de groupe" in person.cong_roles:
                person.short_role = "responsable"
            elif "Adjoint de groupe" in person.cong_roles:
                person.short_role = "adjoint"
            else:
                person.short_role = ""

        return render(
            request,
            "groups/index.html",
            {
                "groups": groups,
                "persons": persons,
            },
        )
