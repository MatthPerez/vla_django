from django import forms
from persons.models import Person


GENDER = (
    ("MALE", "homme"),
    ("FEMALE", "femme"),
)

FUNCTION = (
    ("none", ""),
    ("elder", "ancien"),
    ("assistant", "assistant"),
)

STATUS = (
    ("none", ""),
    ("unbaptized_publisher", "PNB"),
    ("publisher", "PROCL"),
    ("temporary", "PA"),
    ("permanent", "PP"),
    ("special", "PS"),
)


class AddPerson(forms.Form):
    firstname = forms.CharField(
        required=True,
        max_length=100,
        label="Prénom",
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
    cong_status = forms.ChoiceField(
        required=True,
        label="Statut",
        choices=STATUS,
    )
    # TODO :cong_roles, groups


class WeekMeetingForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        optional_fields = [
            "cong_function",
        ]
        for field in optional_fields:
            self.fields[field].required = False
            self.fields[field].widget.attrs.update({"required": False})
