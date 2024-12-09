from django.db import models
from persons.models import Person
from django.utils.timezone import now


class Meeting(models.Model):
    ALLOCATION_TYPES = [
        ("FIRST_CONTACT", "1er contact"),
        ("RETURN_VISIT", "Nouvelle visite"),
        ("STUDY", "Cours biblique"),
        ("DISCUSS", "Discussion"),
        ("SPEECH", "Discours"),
        ("VIDEO", "Vidéo"),
    ]

    id = models.BigAutoField(primary_key=True)
    date = models.DateField(
        default=now,
    )
    president = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="meetings_as_president",
    )
    prayer1 = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="meetings_as_prayer1",
    )
    prayer2 = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="meetings_as_prayer2",
    )
    song1 = models.IntegerField()
    song2 = models.IntegerField()
    song3 = models.IntegerField()
    portion = models.CharField(
        max_length=150,
    )
    jewels = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="meetings_as_jewels",
    )
    jewels_title = models.CharField(
        max_length=150,
    )
    pearls = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="meetings_as_pearls",
    )
    reading1 = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="meetings_as_reading1",
    )
    reading2 = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="meetings_as_reading2",
        blank=True,
        null=True,
    )
    reading3 = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="meetings_as_reading3",
        blank=True,
        null=True,
    )
    advisor2 = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="meetings_as_advisor2",
        blank=True,
        null=True,
    )
    advisor3 = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="meetings_as_advisor3",
        blank=True,
        null=True,
    )
    alloc1_type = models.CharField(
        max_length=20,
        choices=ALLOCATION_TYPES,
    )
    alloc2_type = models.CharField(
        max_length=20,
        choices=ALLOCATION_TYPES,
    )
    alloc3_type = models.CharField(
        max_length=20,
        choices=ALLOCATION_TYPES,
        blank=True,
        null=True,
    )
    alloc4_type = models.CharField(
        max_length=20,
        choices=ALLOCATION_TYPES,
        blank=True,
        null=True,
    )
    alloc1_duration = models.IntegerField()
    alloc2_duration = models.IntegerField()
    alloc3_duration = models.IntegerField(
        blank=True,
        null=True,
    )
    alloc4_duration = models.IntegerField(
        blank=True,
        null=True,
    )
    alloc1pupil_hall1 = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="meetings_as_a1p_h1",
    )
    alloc1inter_hall1 = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="meetings_as_a1i_h1",
        blank=True,
        null=True,
    )
    alloc2pupil_hall1 = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="meetings_as_a2p_h1",
    )
    alloc2inter_hall1 = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="meetings_as_a2i_h1",
        blank=True,
        null=True,
    )
    alloc3pupil_hall1 = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="meetings_as_a3p_h1",
        blank=True,
        null=True,
    )
    alloc3inter_hall1 = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="meetings_as_a3i_h1",
        blank=True,
        null=True,
    )
    alloc4pupil_hall1 = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="meetings_as_a4p_h1",
        blank=True,
        null=True,
    )
    alloc4inter_hall1 = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="meetings_as_a4i_h1",
        blank=True,
        null=True,
    )
    alloc1pupil_hall2 = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="meetings_as_a1p_h2",
        blank=True,
        null=True,
    )
    alloc1inter_hall2 = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="meetings_as_a1i_h2",
        blank=True,
        null=True,
    )
    alloc2pupil_hall2 = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="meetings_as_a2p_h2",
        blank=True,
        null=True,
    )
    alloc2inter_hall2 = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="meetings_as_a2i_h2",
        blank=True,
        null=True,
    )
    alloc3pupil_hall2 = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="meetings_as_a3p_h2",
        blank=True,
        null=True,
    )
    alloc3inter_hall2 = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="meetings_as_a3i_h2",
        blank=True,
        null=True,
    )
    alloc4pupil_hall2 = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="meetings_as_a4p_h2",
        blank=True,
        null=True,
    )
    alloc4inter_hall2 = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="meetings_as_a4i_h2",
        blank=True,
        null=True,
    )
    pupil0_hall3 = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="meetings_as_a0p_h3",
        blank=True,
        null=True,
    )
    inter0_hall3 = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="meetings_as_a0i_h3",
        blank=True,
        null=True,
    )
    pupil_hall3 = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="meetings_as_a1p_h3",
        blank=True,
        null=True,
    )
    vcm1 = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="meetings_as_vcm1",
    )
    vcm2 = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="meetings_as_vcm2",
        blank=True,
        null=True,
    )
    vcm3 = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="meetings_as_vcm3",
        blank=True,
        null=True,
    )
    vcm1_duration = models.IntegerField()
    vcm2_duration = models.IntegerField(
        blank=True,
        null=True,
    )
    vcm3_duration = models.IntegerField(
        blank=True,
        null=True,
    )
    vcm1_title = models.TextField(max_length=100)
    vcm2_title = models.TextField(
        max_length=100,
        blank=True,
        null=True,
    )
    vcm3_title = models.TextField(
        max_length=100,
        blank=True,
        null=True,
    )
    eba = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="meetings_as_eba",
        blank=True,
        null=True,
    )
    eba_reader = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="meetings_as_eba_reader",
        blank=True,
        null=True,
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
