from django.db import models
from persons.models import Person


class Note(models.Model):

    title = models.CharField(
        max_length=100,
    )
    writer = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="writer",
    )
    content = models.CharField(
        max_length=255,
    )
    link = models.CharField(
        max_length=255,
    )

    def __str__(self):
        return self.title
