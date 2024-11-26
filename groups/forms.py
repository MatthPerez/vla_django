from django import forms
from groups.models import Group


class AddGroup(forms.Form):
    name = forms.CharField(
        required=False,
        label="Nom",
        max_length=100,
        widget=forms.DateInput(
            attrs={
                "autofocus": "autofocus",
            },
        ),
    )


class GroupForm(forms.ModelForm):

    class Meta:
        model = Group
        fields = "__all__"
