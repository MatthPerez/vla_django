from django import forms
from django.contrib.auth import authenticate
from .models import CustomUser


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


class SigninForm(forms.Form):
    email = forms.EmailField(label="Email")
    password = forms.CharField(
        widget=forms.PasswordInput,
        label="Mot de passe",
    )

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        if email and password:
            user = authenticate(email=email, password=password)
            if user is None:
                raise forms.ValidationError("Email ou mot de passe incorrect.")
        return self.cleaned_data
