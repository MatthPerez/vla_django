from django import forms
from persons.models import Person
from predication.models import PredicationMeeting


class AddPredicationMeeting(forms.Form):
    date = forms.DateField(
        required=True,
        label="Date",
        input_formats=["%Y-%m-%d"],
        widget=forms.DateInput(
            format="%Y-%m-%d",
            attrs={
                "type": "date",
                "placeholder": "AAAA-MM-JJ",
                "autofocus": "autofocus",
            },
        ),
    )
    manager1 = forms.ModelChoiceField(
        required=False,
        queryset=Person.objects.filter(gender="MALE"),
        widget=forms.Select,
        label="Responsable",
        to_field_name="id",
    )
    place1 = forms.CharField(
        required=True,
        initial="Salle du Royaume",
        max_length=100,
        label="Lieu",
    )
    time1 = forms.CharField(
        required=True,
        max_length=10,
        label="Heure",
        initial="9h15",
    )
    manager2 = forms.ModelChoiceField(
        required=False,
        queryset=Person.objects.filter(gender="MALE"),
        widget=forms.Select,
        label="Responsable",
        to_field_name="id",
    )
    place2 = forms.CharField(
        required=False,
        initial="Salle du Royaume",
        max_length=100,
        label="Lieu",
    )
    time2 = forms.CharField(
        required=False,
        max_length=10,
        label="Heure",
        initial="14h15",
    )
    manager3 = forms.ModelChoiceField(
        required=False,
        queryset=Person.objects.filter(gender="MALE"),
        widget=forms.Select,
        label="Responsable",
        to_field_name="id",
    )
    place3 = forms.CharField(
        required=False,
        initial="Salle du Royaume",
        max_length=100,
        label="Lieu",
    )
    time3 = forms.CharField(
        required=False,
        max_length=10,
        label="Heure",
        initial="17h30",
    )

    def __init__(self, *args, **kwargs):
        super(AddPredicationMeeting, self).__init__(*args, **kwargs)

        fields_with_fullname = [
            "manager1",
            "manager2",
            "manager3",
        ]

        for field in fields_with_fullname:
            if field in self.fields:
                self.fields[field].label_from_instance = lambda obj: obj.fullname


class PredicationMeetingForm(forms.ModelForm):

    class Meta:
        model = PredicationMeeting
        fields = "__all__"
        widgets = {
            "date": forms.DateInput(
                attrs={
                    "type": "date",
                    "placeholder": "AAAA-MM-JJ",
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["date"].input_formats = ["%Y-%m-%d"]
