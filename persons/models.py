from django.db import models


class Person(models.Model):
    GENDERS = [
        ("MALE", "homme"),
        ("FEMALE", "femme"),
    ]

    firstname = models.TextField(max_length=50)
    lastname = models.TextField(max_length=50)
    gender = models.CharField(max_length=6, choices=GENDERS, default="MALE")
    cong_functions = models.TextField(
        max_length=20,
        blank=True,
        null=True,
    )  # Ancien, assistant
    cong_roles = models.JSONField(
        models.TextField(max_length=100),
    )  # Responsable aux territoire, responsable de la sono, etc.
    cong_status = models.TextField(
        max_length=5,
        blank=True,
        null=True,
    )  # PP, PA, PROCL, PNB, EXC
    group = models.TextField(
        max_length=50,
        blank=True,
        null=True,
    )

    @property
    def fullname(self):
        return f"{self.firstname} {self.lastname.upper()}"
