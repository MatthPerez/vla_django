from django.views.generic import ListView, DetailView
from persons.models import Person


class PersonsView(ListView):
    model = Person
    template_name = "persons/index.html"
    context_object_name = "persons"


class PersonsDetail(DetailView):
    model = Person
    template_name = "persons/detail.html"
    context_object_name = "persons"
