from django.db import models
from persons.models import Person
from django.utils.timezone import now


class WeekendMeeting(models.Model):
    date = models.DateField(default=now)
    president = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="meetings_as_we_president",
    )
    song1 = models.IntegerField()
    song2 = models.IntegerField()
    song3 = models.IntegerField()
    speaker = models.ForeignKey(
        Person,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="meetings_as_we_speaker",
    )
    foreign_speaker = models.TextField(
        max_length=100,
        blank=True,
        null=True,
    )
    speech_title = models.TextField(
        max_length=150,
        blank=True,
        null=True,
    )
    watchtower = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="meetings_as_we_watchtower",
    )
    watchtower_reader = models.ForeignKey(
        Person,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="meetings_as_we_watchtower_reader",
    )
    supervisor = models.TextField(
        max_length=100,
        blank=True,
        null=True,
    )
    special_speech = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
