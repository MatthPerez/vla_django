from django.db import models
from persons.models import Person


class Command(models.Model):

    name = models.CharField(
        max_length=50,
    )
    person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="person",
    )