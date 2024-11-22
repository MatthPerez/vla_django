from django.db import models
from django.utils.timezone import now


class Communication(models.Model):
    CATEGORIES = (
        ("CONGREGATION", "Assemblée locale"),
        ("CONVENTION", "Assemblée"),
        ("MAIL", "Courrier"),
        ("LINK", "Lien Internet"),
        ("MISCELLANEOUS", "Divers"),
    )

    id = models.AutoField(primary_key=True)
    date = models.DateField(
        default=now,
    )
    title = models.CharField(max_length=255)
    category = models.CharField(
        max_length=60,
        choices=CATEGORIES,
    )
    content1 = models.TextField(max_length=255)
    content2 = models.TextField(max_length=255)
    content3 = models.TextField(max_length=255)
