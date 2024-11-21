from django.db import models
from groups.models import Group


class Role(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Person(models.Model):
    GENDER = (
        ("MALE", "Homme"),
        ("FEMALE", "Femme"),
    )

    FUNCTION = (
        ("NONE", ""),
        ("ELDER", "Ancien"),
        ("ASSISTANT", "Assistant"),
    )

    ROLES = (
        ("COORDINATOR", "Coordinateur"),
        ("SECRETARY", "Secrétaire"),
        ("PRED_RESP", "Responsable de la prédication"),
        ("GROUP_RESP", "Responsable de groupe"),
        ("GROUP_ADJ", "Adjoint de groupe"),
        ("GROUP_PREP", "Préposé de groupe"),
        ("TERR_RESP", "Responsable aux territoires"),
        ("TERR_ADJ", "Adjoint aux territoires"),
        ("BOOKS_RESP", "Responsable aux publications"),
        ("BOOKS_ADJ", "Adjoint aux publications"),
        ("CONSEILLOR", "Conseiller adjoint"),
        ("WATCHTOWER_RESP", "Responsable à la Tour de Garde"),
        ("VCM_RESP", "Responsable à la VCM"),
        ("VCM_ADJ", "Adjoint à la VCM"),
        ("WEEKEND_RESP", "Responsable des réunions du week-end"),
        ("WEEKEND_ADJ", "Adjoint aux réunions du week-end"),
        ("WELCOME_RESP", "Responsable de l'accueil"),
        ("WELCOME_MEMBER", "Membre de l'accueil"),
        ("SONO_RESP", "Responsable de la sono"),
        ("SONO_MEMBER", "Membre de la sono"),
        ("PODIUM", "Estrade"),
        ("MICRO", "Perche"),
        ("CLH", "CLH"),
        ("GESTION_RESP", "Responsable du Comité de gestion"),
        ("GESTION_MEMBER", "Membre du Comité de gestion"),
        ("MAINTENANCE_RESP", "Coordinateur à la maintenance"),
        ("CLEANING_RESP", "Coordinateur à l'entretien"),
        ("GREEN_SPACES_RESP", "Responsable des travaux d'espaces verts"),
        ("ACCOUNT_RESP", "Responsable aux comptes"),
        ("ACCOUNT_ADJ", "Adjoint aux comptes"),
        ("TREASURER", "Trésorier"),
        ("BOARD_RESP", "Responsable du tableau d'affichage"),
    )

    STATUS = (
        ("NONE", ""),
        ("UNBAPT_PUBLISHER", "PNB"),
        ("PUBLISHER", "PROCL"),
        ("TEMPORARY", "PA"),
        ("PERMANENT", "PP"),
        ("SPECIAL", "PS"),
    )

    firstname = models.CharField(
        max_length=100,
        verbose_name="Prénom",
    )
    lastname = models.CharField(
        max_length=100,
        verbose_name="Nom",
    )
    gender = models.CharField(
        max_length=6,
        choices=GENDER,
        verbose_name="Genre",
    )
    cong_function = models.CharField(
        max_length=9,
        choices=FUNCTION,
        verbose_name="Fonction",
        blank=True,
        null=True,
    )
    cong_roles = models.CharField(
        max_length=255,
        verbose_name="Rôles",
        blank=True,
        null=True,
    )
    cong_status = models.CharField(
        max_length=16,
        choices=STATUS,
        verbose_name="Statut",
        blank=True,
        null=True,
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        verbose_name="Groupe",
        blank=True,
        null=True,
    )

    def get_roles_as_list(self):
        return self.cong_roles.split(",") if self.cong_roles else []

    property

    def fullname(self):
        return f"{self.firstname} {self.lastname.upper()}"
