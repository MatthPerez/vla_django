from django import forms
from vcm.models import Meeting
from persons.models import Person


ALLOC_TYPES = (
    ("FIRST_CONTACT", "1er contact"),
    ("RETURN_VISIT", "Nouvelle visite"),
    ("STUDY", "Cours biblique"),
    ("DISCUSS", "Discussion"),
    ("SPEECH", "Discours"),
    ("VIDEO", "Vidéo"),
)


class AddMeeting(forms.Form):
    # password = CharField(
    #     max_lenght=8,
    #     widget=forms.PasswordInput(),
    #     required=True,
    # )
    date = forms.DateField(
        required=True,
        label="Date",
        input_formats=["%Y-%m-%d"],
        widget=forms.DateInput(
            attrs={
                "type": "date",
                "autofocus": "autofocus",
            },
        ),
    )
    president = forms.ModelChoiceField(
        required=True,
        queryset=Person.objects.filter(cong_functions__icontains="ancien"),
        widget=forms.Select,
        label="Président",
        to_field_name="id",
    )
    prayer1 = forms.ModelChoiceField(
        required=True,
        queryset=Person.objects.filter(gender="MALE"),
        widget=forms.Select,
        label="Prière initiale",
        to_field_name="id",
    )
    prayer2 = forms.ModelChoiceField(
        required=True,
        queryset=Person.objects.filter(gender="MALE"),
        widget=forms.Select,
        label="Prière finale",
        to_field_name="id",
    )
    song1 = forms.IntegerField(
        required=True,
        label="Cantique initial",
    )
    song2 = forms.IntegerField(
        required=True,
        label="Cantique intermédiaire",
    )
    song3 = forms.IntegerField(
        required=True,
        label="Cantique final",
    )
    portion = forms.CharField(
        required=True,
        label="Portion à lire",
        max_length=100,
    )
    jewels = forms.ModelChoiceField(
        required=True,
        queryset=Person.objects.exclude(cong_functions=""),
        widget=forms.Select,
        label="Joyaux (orateur)",
    )
    jewels_title = forms.CharField(
        required=True,
        label="Joyaux (titre)",
        max_length=100,
    )
    pearls = forms.ModelChoiceField(
        required=True,
        queryset=Person.objects.exclude(cong_functions=""),
        widget=forms.Select,
        label="Perles",
        to_field_name="id",
    )
    reading1 = forms.ModelChoiceField(
        required=True,
        queryset=Person.objects.filter(gender="MALE"),
        widget=forms.Select,
        label="Lecture",
        to_field_name="id",
    )
    reading2 = forms.ModelChoiceField(
        required=False,
        queryset=Person.objects.filter(gender="MALE"),
        widget=forms.Select,
        label="Lecture",
        to_field_name="id",
    )
    reading3 = forms.ModelChoiceField(
        required=False,
        queryset=Person.objects.filter(gender="MALE"),
        widget=forms.Select,
        label="Lecture",
        to_field_name="id",
    )
    advisor2 = forms.ModelChoiceField(
        required=False,
        queryset=Person.objects.filter(cong_functions__icontains="ancien"),
        widget=forms.Select,
        label="Conseiller",
        to_field_name="id",
    )
    advisor3 = forms.ModelChoiceField(
        required=False,
        queryset=Person.objects.filter(cong_functions__icontains="ancien"),
        widget=forms.Select,
        label="Conseiller",
        to_field_name="id",
    )
    alloc1_type = forms.ChoiceField(
        required=True,
        label="Type sujet 1",
        choices=ALLOC_TYPES,
    )
    alloc2_type = forms.ChoiceField(
        required=True,
        label="Type sujet 2",
        choices=ALLOC_TYPES,
    )
    alloc3_type = forms.ChoiceField(
        required=False,
        label="Type sujet 3",
        choices=ALLOC_TYPES,
    )
    alloc4_type = forms.ChoiceField(
        required=False,
        label="Type sujet 4",
        choices=ALLOC_TYPES,
    )
    alloc1_duration = forms.IntegerField(
        required=True,
        label="Durée sujet 1",
    )
    alloc2_duration = forms.IntegerField(
        required=True,
        label="Durée sujet 2",
    )
    alloc3_duration = forms.IntegerField(
        required=False,
        label="Durée sujet 3",
    )
    alloc4_duration = forms.IntegerField(
        required=False,
        label="Durée sujet 4",
    )
    alloc1pupil_hall1 = forms.ModelChoiceField(
        required=False,
        queryset=Person.objects.all(),
        widget=forms.Select,
        label="Sujet 1 élève",
        to_field_name="id",
    )
    alloc1inter_hall1 = forms.ModelChoiceField(
        required=False,
        queryset=Person.objects.all(),
        widget=forms.Select,
        label="Sujet 1 interlocuteur",
        to_field_name="id",
    )
    alloc2pupil_hall1 = forms.ModelChoiceField(
        required=False,
        queryset=Person.objects.all(),
        widget=forms.Select,
        label="Sujet 2 élève",
        to_field_name="id",
    )
    alloc2inter_hall1 = forms.ModelChoiceField(
        required=False,
        queryset=Person.objects.all(),
        widget=forms.Select,
        label="Sujet 2 interlocuteur",
        to_field_name="id",
    )
    alloc3pupil_hall1 = forms.ModelChoiceField(
        required=False,
        queryset=Person.objects.all(),
        widget=forms.Select,
        label="Sujet 3 élève",
        to_field_name="id",
    )
    alloc3inter_hall1 = forms.ModelChoiceField(
        required=False,
        queryset=Person.objects.all(),
        widget=forms.Select,
        label="Sujet 3 interlocuteur",
        to_field_name="id",
    )
    alloc4pupil_hall1 = forms.ModelChoiceField(
        required=False,
        queryset=Person.objects.all(),
        widget=forms.Select,
        label="Sujet 4 élève",
        to_field_name="id",
    )
    alloc4inter_hall1 = forms.ModelChoiceField(
        required=False,
        queryset=Person.objects.all(),
        widget=forms.Select,
        label="Sujet 4 interlocuteur",
        to_field_name="id",
    )
    alloc1pupil_hall2 = forms.ModelChoiceField(
        required=False,
        queryset=Person.objects.all(),
        widget=forms.Select,
        label="Sujet 1 élève",
        to_field_name="id",
    )
    alloc1inter_hall2 = forms.ModelChoiceField(
        required=False,
        queryset=Person.objects.all(),
        widget=forms.Select,
        label="Sujet 1 interlocuteur",
        to_field_name="id",
    )
    alloc2pupil_hall2 = forms.ModelChoiceField(
        required=False,
        queryset=Person.objects.all(),
        widget=forms.Select,
        label="Sujet 2 élève",
        to_field_name="id",
    )
    alloc2inter_hall2 = forms.ModelChoiceField(
        required=False,
        queryset=Person.objects.all(),
        widget=forms.Select,
        label="Sujet 2 interlocuteur",
        to_field_name="id",
    )
    alloc3pupil_hall2 = forms.ModelChoiceField(
        required=False,
        queryset=Person.objects.all(),
        widget=forms.Select,
        label="Sujet 3 élève",
        to_field_name="id",
    )
    alloc3inter_hall2 = forms.ModelChoiceField(
        required=False,
        queryset=Person.objects.all(),
        widget=forms.Select,
        label="Sujet 3 interlocuteur",
        to_field_name="id",
    )
    alloc4pupil_hall2 = forms.ModelChoiceField(
        required=False,
        queryset=Person.objects.all(),
        widget=forms.Select,
        label="Sujet 4 élève",
        to_field_name="id",
    )
    alloc4inter_hall2 = forms.ModelChoiceField(
        required=False,
        queryset=Person.objects.all(),
        widget=forms.Select,
        label="Sujet 4 interlocuteur",
        to_field_name="id",
    )
    pupil_hall3 = forms.ModelChoiceField(
        required=False,
        queryset=Person.objects.all(),
        widget=forms.Select,
        label="Discours",
        to_field_name="id",
    )
    vcm1 = forms.ModelChoiceField(
        required=True,
        queryset=Person.objects.exclude(cong_functions=""),
        widget=forms.Select,
        label="Sujet VCM 1",
        to_field_name="id",
    )
    vcm2 = forms.ModelChoiceField(
        required=False,
        queryset=Person.objects.exclude(cong_functions=""),
        widget=forms.Select,
        label="Sujet VCM 2",
        to_field_name="id",
    )
    vcm3 = forms.ModelChoiceField(
        required=False,
        queryset=Person.objects.filter(cong_functions__icontains="ancien"),
        widget=forms.Select,
        label="Sujet VCM 3",
        to_field_name="id",
    )
    vcm1_duration = forms.IntegerField(
        required=True,
        label="Durée sujet VCM 1",
    )
    vcm2_duration = forms.IntegerField(
        required=False,
        label="Durée sujet VCM 2",
    )
    vcm3_duration = forms.IntegerField(
        required=False,
        label="Durée sujet VCM 3",
    )
    vcm1_title = forms.CharField(
        required=True,
        label="Titre sujet VCM 1",
        max_length=100,
    )
    vcm2_title = forms.CharField(
        required=False,
        label="Titre sujet VCM 2",
        max_length=100,
    )
    vcm3_title = forms.CharField(
        required=False,
        label="Titre sujet VCM 3",
        max_length=100,
    )
    eba = forms.ModelChoiceField(
        required=False,
        queryset=Person.objects.filter(cong_functions__icontains="ancien"),
        widget=forms.Select,
        label="Etude biblique de l'assemblée",
        to_field_name="id",
    )
    eba_reader = forms.ModelChoiceField(
        required=False,
        queryset=Person.objects.filter(gender="MALE"),
        widget=forms.Select,
        label="Lecteur",
        to_field_name="id",
    )
    supervisor = forms.CharField(
        required=False,
        label="Responsable de circonscription",
    )
    special_speech = forms.CharField(
        required=False,
        label="Titre du discours spécial",
        max_length=100,
    )

    parking = forms.ModelChoiceField(
        required=False,
        queryset=Person.objects.filter(gender="MALE"),
        widget=forms.Select,
        label="Parking",
        to_field_name="id",
    )
    entrance = forms.ModelChoiceField(
        required=False,
        queryset=Person.objects.filter(gender="MALE"),
        widget=forms.Select,
        label="Entrée",
        to_field_name="id",
    )
    inside = forms.ModelChoiceField(
        required=False,
        queryset=Person.objects.filter(gender="MALE"),
        widget=forms.Select,
        label="Auditorium",
        to_field_name="id",
    )
    podium = forms.ModelChoiceField(
        required=False,
        queryset=Person.objects.filter(gender="MALE"),
        widget=forms.Select,
        label="Estrade",
        to_field_name="id",
    )
    sono1 = forms.ModelChoiceField(
        required=False,
        queryset=Person.objects.filter(gender="MALE"),
        widget=forms.Select,
        label="Sono 1",
        to_field_name="id",
    )
    sono2 = forms.ModelChoiceField(
        required=False,
        queryset=Person.objects.filter(gender="MALE"),
        widget=forms.Select,
        label="Sono 2",
        to_field_name="id",
    )
    mic1 = forms.ModelChoiceField(
        required=False,
        queryset=Person.objects.filter(gender="MALE"),
        widget=forms.Select,
        label="Perche 1",
        to_field_name="id",
    )
    mic2 = forms.ModelChoiceField(
        required=False,
        queryset=Person.objects.filter(gender="MALE"),
        widget=forms.Select,
        label="Perche 2",
        to_field_name="id",
    )

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

    def __init__(self, *args, **kwargs):
        super(AddMeeting, self).__init__(*args, **kwargs)

        fields_with_fullname = [
            "president",
            "prayer1",
            "prayer2",
            "jewels",
            "pearls",
            "reading1",
            "reading2",
            "reading3",
            "advisor2",
            "advisor3",
            "alloc1pupil_hall1",
            "alloc1inter_hall1",
            "alloc2pupil_hall1",
            "alloc2inter_hall1",
            "alloc3pupil_hall1",
            "alloc3inter_hall1",
            "alloc4pupil_hall1",
            "alloc4inter_hall1",
            "alloc1pupil_hall2",
            "alloc1inter_hall2",
            "alloc2pupil_hall2",
            "alloc2inter_hall2",
            "alloc3pupil_hall2",
            "alloc3inter_hall2",
            "alloc4pupil_hall2",
            "alloc4inter_hall2",
            "pupil_hall3",
            "vcm1",
            "vcm2",
            "vcm3",
            "eba",
            "eba_reader",
            "parking",
            "entrance",
            "inside",
            "podium",
            "sono1",
            "sono2",
            "mic1",
            "mic2",
        ]

        for field in fields_with_fullname:
            if field in self.fields:
                self.fields[field].label_from_instance = lambda obj: obj.fullname


class WeekMeetingForm(forms.ModelForm):

    class Meta:
        model = Meeting
        fields = "__all__"
        widgets = {
            "date": forms.DateInput(
                attrs={"type": "date", "placeholder": "AAAA-MM-JJ"}
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        optional_fields = [
            "alloc2inter_hall1",
            "alloc3pupil_hall1",
            "alloc3inter_hall1",
            "alloc4pupil_hall1",
            "alloc4inter_hall1",
            "alloc2pupil_hall2",
            "alloc2inter_hall2",
            "alloc3pupil_hall2",
            "alloc3inter_hall2",
            "alloc4pupil_hall2",
            "alloc4inter_hall2",
            "pupil_hall3",
            "advisor2",
            "advisor3",
            "vcm2",
            "vcm2_title",
            "vcm3",
            "vcm3_title",
            "eba",
            "eba_reader",
            "supervisor",
            "parking",
            "entrance",
            "inside",
            "podium",
            "sono1",
            "sono2",
            "mic1",
            "mic2",
        ]
        for field in optional_fields:
            self.fields[field].required = False
            self.fields[field].widget.attrs.update({"required": False})

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["date"].input_formats = ["%Y-%m-%d"]
