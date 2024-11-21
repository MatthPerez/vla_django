from django import forms
from persons.models import Person
from groups.models import Group


GENDER = (
    ("MALE", "homme"),
    ("FEMALE", "femme"),
)

FUNCTION = (
    ("NONE", ""),
    ("ELDER", "ancien"),
    ("ASSISTANT", "assistant"),
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


class AddPerson(forms.Form):
    firstname = forms.CharField(
        required=True,
        max_length=100,
        label="Prénom",
        widget=forms.TextInput(
            attrs={
                "autofocus": "autofocus",
            }
        ),
    )
    lastname = forms.CharField(
        required=True,
        max_length=100,
        label="Nom",
    )
    gender = forms.ChoiceField(
        required=True,
        label="Genre",
        choices=GENDER,
    )
    cong_function = forms.ChoiceField(
        required=True,
        label="Fonction",
        choices=FUNCTION,
    )
    cong_roles = forms.MultipleChoiceField(
        required=False,
        label="Rôles",
        choices=sorted(ROLES, key=lambda x: x[1]),
        widget=forms.CheckboxSelectMultiple,
    )
    cong_status = forms.ChoiceField(
        required=True,
        label="Statut",
        choices=STATUS,
    )
    group = forms.ModelChoiceField(
        required=True,
        label="Groupe",
        queryset=Group.objects.all()
    )


class PersonForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        optional_fields = [
            "firstname",
            "lastname",
            "gender",
        ]
        for field in optional_fields:
            self.fields[field].required = False
            self.fields[field].widget.attrs.update({"required": False})
