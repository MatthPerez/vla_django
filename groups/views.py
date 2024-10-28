from django.shortcuts import render
from django.views import View


class GroupsView(View):
    def get(self, request):
        return render(
            request,
            "groups/index.html",
        )
