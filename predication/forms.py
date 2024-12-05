from django import forms
from persons.models import Person
from predication.models import PredicationMeeting


class AddPredicationMeeting(forms.Form):
    date = forms.CharField(
        required=True,
        label="Date",
        max_length=100,
        widget=forms.DateInput(
            attrs={
                "autofocus": "autofocus",
            },
        ),
    )
    manager = forms.ModelChoiceField(
        required=True,
        queryset=Person.objects.filter(gender="MALE"),
        widget=forms.Select,
        label="Responsable",
        to_field_name="id",
    )
    place = forms.CharField(
        required=True,
        max_length=100,
        label="Lieu",
    )
    time = forms.CharField(
        required=True,
        max_length=10,
        label="Heure",
    )


class PredicationMeetingForm(forms.ModelForm):

    class Meta:
        model = PredicationMeeting
        fields = "__all__"
