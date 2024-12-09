from django import forms
from commands.models import Command
from publications.models import Publication
from persons.models import Person


class AddCommand(forms.Form):
    person = forms.ModelChoiceField(
        required=True,
        queryset=Person.objects.all(),
        widget=forms.Select(
            attrs={
                "class": "form-control",
                "autofocus": "autofocus",
            }
        ),
        label="Destinataire",
    )
    publication = forms.ModelChoiceField(
        required=True,
        queryset=Publication.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        label="Publication",
    )

    def __init__(self, *args, **kwargs):
        super(AddCommand, self).__init__(*args, **kwargs)

        self.fields["person"].label_from_instance = lambda obj: obj.fullname
        self.fields["publication"].label_from_instance = lambda obj: obj.name


class CommandForm(forms.ModelForm):
    class Meta:
        model = Command
        fields = "__all__"
        widgets = {
            "person": forms.Select(attrs={"class": "form-control"}),
            "publication": forms.Select(attrs={"class": "form-control"}),
        }
