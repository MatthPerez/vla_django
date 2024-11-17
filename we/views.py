from django.views.generic import ListView
from we.models import WeekendMeeting
from django.utils import timezone


class WeMeetingView(ListView):
    model = WeekendMeeting
    template_name = "we/index.html"
    context_object_name = "meetings"

    def get_queryset(self):
        now = timezone.now()

        return WeekendMeeting.objects.filter(date__gte=now)