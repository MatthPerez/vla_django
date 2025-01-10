from django.db import models
from persons.models import Person
from django.utils.timezone import now
import locale

locale.setlocale(locale.LC_TIME, "fr_FR.UTF-8")


class PredicationMeeting(models.Model):

    date = models.DateField(
        default=now,
    )
    time = models.TextField(
        max_length=10,
    )
    manager = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="manager",
        null=True,
        blank=True,
    )
    place = models.TextField(
        max_length=255,
    )

    @property
    def day(self):
        return self.date.strftime("%A")

    def __str__(self):
        return f"{self.date} {self.time}"
