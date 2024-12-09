from django.db import models
from persons.models import Person
from publications.models import Publication


class Command(models.Model):

    person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="person",
    )
    publication = models.ForeignKey(
        Publication,
        on_delete=models.CASCADE,
        related_name="publication",
    )