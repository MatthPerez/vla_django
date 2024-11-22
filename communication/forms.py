from django import forms
from communication.models import Communication
from django.db.models import Q


CATEGORIES = (
    ("CONGREGATION", "Assemblée locale"),
    ("CONVENTION", "Assemblée"),
    ("MAIL", "Courrier"),
    ("LINK", "Lien Internet"),
    ("MISCELLANEOUS", "Divers"),
)


class AddCommunication(forms.Form):
    date = forms.DateField(
        required=True,
        label="Date",
        input_formats=["%Y-%m-%d"],
        widget=forms.DateInput(
            attrs={
                "type": "date",
                "autofocus": "autofocus",
            },
        ),
    )
    title = forms.CharField(
        required=True,
        label="Titre",
        max_length=255,
    )
    category = forms.ChoiceField(
        required=True,
        label="Statut",
        choices=CATEGORIES,
    )
    content1 = forms.CharField(
        required=True,
        label="Contenu 1",
        max_length=255,
    )
    content2 = forms.CharField(
        required=True,
        label="Contenu 2",
        max_length=255,
    )
    content3 = forms.CharField(
        required=True,
        label="Contenu 3",
        max_length=255,
    )


class WeekMeetingForm(forms.ModelForm):

    class Meta:
        model = Communication
        fields = "__all__"
        widgets = {
            "date": forms.DateInput(
                attrs={"type": "date", "placeholder": "AAAA-MM-JJ"}
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        optional_fields = [
            "content2",
            "content3",
        ]
        for field in optional_fields:
            self.fields[field].required = False
            self.fields[field].widget.attrs.update({"required": False})

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["date"].input_formats = ["%Y-%m-%d"]
