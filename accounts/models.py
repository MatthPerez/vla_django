from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    username = models.CharField(
        unique=True,
        max_length=100,
    )
    email = models.EmailField(
        max_length=100,
    )
    password = models.CharField(
        max_length=20,
    )
