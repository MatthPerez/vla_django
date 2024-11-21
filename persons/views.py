from django.views.generic import ListView, DetailView
from persons.models import Person


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
