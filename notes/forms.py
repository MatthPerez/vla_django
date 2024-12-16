from django import forms
from notes.models import Note


class AddNote(forms.Form):
    title = forms.CharField(
        required=True,
        label="Titre",
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "autofocus": "autofocus",
            },
        ),
    )
    content = forms.CharField(
        required=True,
        label="Contenu",
        max_length=255,
    )
    link = forms.CharField(
        required=False,
        label="Lien Internet",
        max_length=255,
    )


class NoteForm(forms.ModelForm):

    class Meta:
        model = Note
        fields = "__all__"
