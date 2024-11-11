from django import forms
from vcm.models import Meeting


ALLOC_TYPES = (
    ("FIRST_CONTACT", "1er contact"),
    ("RETURN_VISIT", "Nouvelle visite"),
    ("STUDY", "Cours biblique"),
    ("DISCUSS", "Discussion"),
    ("SPEECH", "Discours"),
    ("VIDEO", "Vidéo"),
)


class AddMeeting(forms.Form):
    # password = CharField(max_lenght=8, widget=forms.PasswordInput(), required=True)
    date = forms.DateField(required=True)
    president = forms.CharField(max_length=100, required=True)
    prayer1 = forms.CharField(max_length=100, required=True)
    prayer2 = forms.CharField(max_length=100, required=True)
    song1 = forms.IntegerField(required=True)
    song2 = forms.IntegerField(required=True)
    song3 = forms.IntegerField(required=True)
    portion = forms.CharField(max_length=100, required=True)
    jewels = forms.CharField(max_length=100, required=True)
    jewels_title = forms.CharField(max_length=100, required=True)
    pearls = forms.CharField(max_length=100, required=True)
    reading1 = forms.ChoiceField(choices=ALLOC_TYPES, required=True)
    reading2 = forms.ChoiceField(choices=ALLOC_TYPES, required=False)
    reading3 = forms.ChoiceField(choices=ALLOC_TYPES, required=False)
    alloc1_type = forms.CharField(max_length=100, required=True)
    alloc2_type = forms.CharField(max_length=100, required=True)
    alloc3_type = forms.CharField(max_length=100, required=False)
    alloc4_type = forms.CharField(max_length=100, required=False)
    alloc1_duration = forms.CharField(max_length=100, required=True)
    alloc2_duration = forms.CharField(max_length=100, required=True)
    alloc3_duration = forms.CharField(max_length=100, required=False)
    alloc4_duration = forms.CharField(max_length=100, required=False)
    alloc1pupil_hall1 = forms.CharField(max_length=100, required=True)
    alloc1inter_hall1 = forms.CharField(max_length=100, required=False)
    alloc2pupil_hall1 = forms.CharField(max_length=100, required=True)
    alloc2inter_hall1 = forms.CharField(max_length=100, required=True)
    alloc3pupil_hall1 = forms.CharField(max_length=100, required=True)
    alloc3inter_hall1 = forms.CharField(max_length=100, required=False)
    alloc4pupil_hall1 = forms.CharField(max_length=100, required=False)
    alloc4inter_hall1 = forms.CharField(max_length=100, required=False)
    alloc1pupil_hall2 = forms.CharField(max_length=100, required=False)
    alloc1inter_hall2 = forms.CharField(max_length=100, required=False)
    alloc2pupil_hall2 = forms.CharField(max_length=100, required=False)
    alloc2inter_hall2 = forms.CharField(max_length=100, required=False)
    alloc3pupil_hall2 = forms.CharField(max_length=100, required=False)
    alloc4pupil_hall2 = forms.CharField(max_length=100, required=False)
    alloc4inter_hall2 = forms.CharField(max_length=100, required=False)
    alloc3inter_hall2 = forms.CharField(max_length=100, required=False)
    alloc1pupil_hall3 = forms.CharField(max_length=100, required=False)
    alloc1inter_hall3 = forms.CharField(max_length=100, required=False)
    alloc2pupil_hall3 = forms.CharField(max_length=100, required=False)
    alloc2inter_hall3 = forms.CharField(max_length=100, required=False)
    alloc3pupil_hall3 = forms.CharField(max_length=100, required=False)
    alloc3inter_hall3 = forms.CharField(max_length=100, required=False)
    alloc4pupil_hall3 = forms.CharField(max_length=100, required=False)
    alloc1pupil_hall3 = forms.CharField(max_length=100, required=False)
    alloc4inter_hall3 = forms.CharField(max_length=100, required=False)
    vcm1 = forms.CharField(max_length=100, required=True)
    vcm2 = forms.CharField(max_length=100, required=False)
    vcm3 = forms.CharField(max_length=100, required=False)
    vcm1_duration = forms.CharField(max_length=100, required=True)
    vcm2_duration = forms.CharField(max_length=100, required=False)
    vcm3_duration = forms.CharField(max_length=100, required=False)
    vcm1_title = forms.CharField(max_length=100, required=True)
    vcm2_title = forms.CharField(max_length=100, required=False)
    vcm3_title = forms.CharField(max_length=100, required=False)
    eba = forms.CharField(max_length=100, required=False)
    eba_reader = forms.CharField(max_length=100, required=False)
    supervisor = forms.CharField(max_length=100, required=False)
    special_speech = forms.CharField(max_length=100, required=False)
    parking = forms.CharField(max_length=100, required=False)
    entrance = forms.CharField(max_length=100, required=False)
    inside = forms.CharField(max_length=100, required=False)
    podium = forms.CharField(max_length=100, required=False)
    sono1 = forms.CharField(max_length=100, required=False)
    sono2 = forms.CharField(max_length=100, required=False)
    mic1 = forms.CharField(max_length=100, required=False)
    mic2 = forms.CharField(max_length=100, required=False)

    def special_week(self):
        eba = self.cleaned_data.get("eba")
        eba_reader = self.cleaned_data.get("eba_reader")
        supervisor = self.cleaned_data.get("supervisor")
        special_speech = self.cleaned_data.get("special_speech")

        if supervisor is not None:
            if special_speech is None:
                raise forms.ValidationError(
                    "Le responsable de circonscription est indiqué mais pas le titre du discours spécial."
                )

            if eba is not None or eba_reader is not None:
                raise forms.ValidationError("Il n'y a pas d'étude biblique ce jour-là.")

            return supervisor


class WeekMeetingForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = "__all__"
