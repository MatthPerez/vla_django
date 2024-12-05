from django.db import models
from persons.models import Person
from django.utils.timezone import now
import locale

locale.setlocale(locale.LC_TIME, "fr_FR.UTF-8")


class PredicationMeeting(models.Model):

    date = models.DateField(
        default=now,
    )
    manager1 = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="manager1",
    )
    place1 = models.TextField(
        max_length=255,
    )
    time1 = models.TextField(
        max_length=10,
    )
    manager2 = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="manager2",
        null=True,
        blank=True,
    )
    place2 = models.TextField(
        max_length=255,
        null=True,
        blank=True,
    )
    time2 = models.TextField(
        max_length=10,
        null=True,
        blank=True,
    )
    manager3 = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="manager3",
        null=True,
        blank=True,
    )
    place3 = models.TextField(
        max_length=255,
        null=True,
        blank=True,
    )
    time3 = models.TextField(
        max_length=10,
        null=True,
        blank=True,
    )

    @property
    def day(self):
        return self.date.strftime("%A")

    def __str__(self):
        return self.date
