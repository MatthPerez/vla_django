from django import forms
from publications.models import Publication


class AddPublication(forms.Form):
    name = forms.CharField(
        required=False,
        label="Nom",
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "autofocus": "autofocus",
            },
        ),
    )


class PublicationForm(forms.ModelForm):

    class Meta:
        model = Publication
        fields = "__all__"
