from django import forms
from accounts.models import CustomUser


class AddCustomUser(forms.Form):
    email = forms.EmailField(
        required=True,
        label="Courriel",
        max_length=255,
        widget=forms.TextInput(
            attrs={
                "autofocus": "autofocus",
            },
        ),
    )
    password = forms.CharField(
        max_length=20,
        widget=forms.PasswordInput(),
        label="Mot de passe",
        required=True,
    )
    first_name = forms.CharField(
        label="Prénom",
        required=True,
    )
    last_name = forms.CharField(
        label="Nom",
        required=True,
    )
    city = forms.CharField(
        label="Ville",
        required=True,
    )


class CustomUserForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = "__all__"
