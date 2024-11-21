from django.shortcuts import render
from django.views import View
from groups.models import Group


class GroupsView(View):
    def get(self, request):
        groups = Group.objects.all().order_by("name")

        
        return render(
            request,
            "groups/index.html",
            {
                "groups": groups,
                "groups": groups,
            },
        )
