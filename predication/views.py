from django.views.generic import ListView
from predication.models import PredicationMeeting


class PredicationView(ListView):
    model = PredicationMeeting
    context_object_name = "meeting"
    template_name = "predication/index.html"
    empty_text = "Aucune réunion trouvée."

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["count"] = self.get_queryset().count()
        context["empty_text"] = self.empty_text
        return context