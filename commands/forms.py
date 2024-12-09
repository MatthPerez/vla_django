from django import forms
from commands.models import Command
from publications.models import Publication
from persons.models import Person


class AddCommand(forms.Form):
    publication = forms.ModelChoiceField(
        required=True,
        queryset=Publication.objects.all(),
        widget=forms.Select,
        label="Publication",
        to_field_name="id",
    )
    person = forms.ModelChoiceField(
        required=True,
        queryset=Person.objects.all(),
        widget=forms.Select,
        label="Destinataire",
        to_field_name="id",
    )

    def __init__(self, *args, **kwargs):
        super(AddCommand, self).__init__(*args, **kwargs)

        fields_with_fullname = [
            "person",
        ]

        for field in fields_with_fullname:
            if field in self.fields:
                self.fields[field].label_from_instance = lambda obj: obj.fullname


class CommandForm(forms.ModelForm):

    class Meta:
        model = Command
        fields = "__all__"
