from django.shortcuts import render
from django.views import View
from persons.models import Person


class PrivateView(View):
    
    def get(self, request):
        persons = Person.objects.all()

        return render(
            request,
            "private/index.html",
            {
                "persons": persons,
            },
        )
