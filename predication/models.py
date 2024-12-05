from django.db import models
from persons.models import Person
from django.utils.timezone import now


class PredicationMeeting(models.Model):

    date = models.DateField(
        default=now,
    )
    manager = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="manager",
    )
    place = models.TextField(
        max_length=255,
    )
    time = models.TextField(
        max_length=10,
    )

    def __str__(self):
        return self.date
