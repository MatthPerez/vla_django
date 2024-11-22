from django.shortcuts import render
from django.views import View
from groups.models import Group
from persons.models import Person


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
