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
    # password = CharField(max_lenght=8, widget=forms.PasswordInput(), required=True)
    date = forms.DateField(
        label="Date",
        required=True,
        input_formats=["%d-%m-%Y"],
        widget=forms.DateInput(
            format="%d-%m-%Y", attrs={"type": "date", "autofocus": "autofocus"}
        ),
    )
    president = forms.ModelChoiceField(
        queryset=Person.objects.filter(cong_functions__icontains="ancien"),
        widget=forms.Select,
        label="Président",
        to_field_name="id",
    )
    prayer1 = forms.ModelChoiceField(
        queryset=Person.objects.filter(gender="MALE"),
        widget=forms.Select,
        label="Prière initiale",
        to_field_name="id",
    )
    prayer2 = forms.ModelChoiceField(
        queryset=Person.objects.filter(gender="MALE"),
        widget=forms.Select,
        label="Prière finale",
        to_field_name="id",
    )
    song1 = forms.IntegerField(label="Cantique initial", required=True)
    song2 = forms.IntegerField(label="Cantique intermédiaire", required=True)
    song3 = forms.IntegerField(label="Cantique final", required=True)
    portion = forms.CharField(label="Portion à lire", max_length=100, required=True)
    jewels = forms.ModelChoiceField(
        queryset = Person.objects.exclude(cong_functions=""),
        widget=forms.Select,
        label="Joyaux (orateur)",
    )
    jewels_title = forms.CharField(
        label="Joyaux (titre)", max_length=100, required=True
    )
    pearls = forms.ModelChoiceField(
        queryset=Person.objects.exclude(cong_functions=""),
        widget=forms.Select,
        label="Perles",
        to_field_name="id",
    )
    reading1 = forms.ModelChoiceField(
        queryset=Person.objects.filter(gender="MALE"),
        widget=forms.Select,
        label="Lecture",
        to_field_name="id",
    )
    reading2 = forms.ModelChoiceField(
        queryset=Person.objects.filter(gender="MALE"),
        widget=forms.Select,
        label="Lecture",
        to_field_name="id",
    )
    reading3 = forms.ModelChoiceField(
        queryset=Person.objects.filter(gender="MALE"),
        widget=forms.Select,
        label="Lecture",
        to_field_name="id",
    )
    advisor2 = forms.ModelChoiceField(
        queryset=Person.objects.filter(cong_functions__icontains="ancien"),
        widget=forms.Select,
        label="Conseiller",
        to_field_name="id",
    )
    advisor3 = forms.ModelChoiceField(
        queryset=Person.objects.filter(cong_functions__icontains="ancien"),
        widget=forms.Select,
        label="Conseiller",
        to_field_name="id",
    )
    alloc1_type = forms.ChoiceField(
        label="Type sujet 1", choices=ALLOC_TYPES, required=True
    )
    alloc2_type = forms.ChoiceField(
        label="Type sujet 2", choices=ALLOC_TYPES, required=True
    )
    alloc3_type = forms.ChoiceField(
        label="Type sujet 3", choices=ALLOC_TYPES, required=True
    )
    alloc4_type = forms.ChoiceField(
        label="Type sujet 4", choices=ALLOC_TYPES, required=True
    )
    alloc1_duration = forms.CharField(
        label="Durée sujet 1", max_length=100, required=True
    )
    alloc2_duration = forms.CharField(
        label="Durée sujet 2", max_length=100, required=True
    )
    alloc3_duration = forms.CharField(
        label="Durée sujet 3", max_length=100, required=False
    )
    alloc4_duration = forms.CharField(
        label="Durée sujet 4", max_length=100, required=False
    )

    alloc1pupil_hall1 = forms.ModelChoiceField(
        queryset=Person.objects.all(),
        widget=forms.Select,
        label="Sujet 1 élève",
        to_field_name="id",
    )
    alloc1inter_hall1 = forms.ModelChoiceField(
        queryset=Person.objects.all(),
        widget=forms.Select,
        label="Sujet 1 interlocuteur",
        to_field_name="id",
    )
    alloc2pupil_hall1 = forms.ModelChoiceField(
        queryset=Person.objects.all(),
        widget=forms.Select,
        label="Sujet 2 élève",
        to_field_name="id",
    )
    alloc2inter_hall1 = forms.ModelChoiceField(
        queryset=Person.objects.all(),
        widget=forms.Select,
        label="Sujet 2 interlocuteur",
        to_field_name="id",
    )
    alloc3pupil_hall1 = forms.ModelChoiceField(
        queryset=Person.objects.all(),
        widget=forms.Select,
        label="Sujet 3 élève",
        to_field_name="id",
    )
    alloc3inter_hall1 = forms.ModelChoiceField(
        queryset=Person.objects.all(),
        widget=forms.Select,
        label="Sujet 3 interlocuteur",
        to_field_name="id",
    )
    alloc4pupil_hall1 = forms.ModelChoiceField(
        queryset=Person.objects.all(),
        widget=forms.Select,
        label="Sujet 4 élève",
        to_field_name="id",
    )
    alloc4inter_hall1 = forms.ModelChoiceField(
        queryset=Person.objects.all(),
        widget=forms.Select,
        label="Sujet 4 interlocuteur",
        to_field_name="id",
    )
    alloc1pupil_hall2 = forms.ModelChoiceField(
        queryset=Person.objects.all(),
        widget=forms.Select,
        label="Sujet 1 élève",
        to_field_name="id",
    )
    alloc1inter_hall2 = forms.ModelChoiceField(
        queryset=Person.objects.all(),
        widget=forms.Select,
        label="Sujet 1 interlocuteur",
        to_field_name="id",
    )
    alloc2pupil_hall2 = forms.ModelChoiceField(
        queryset=Person.objects.all(),
        widget=forms.Select,
        label="Sujet 2 élève",
        to_field_name="id",
    )
    alloc2inter_hall2 = forms.ModelChoiceField(
        queryset=Person.objects.all(),
        widget=forms.Select,
        label="Sujet 2 interlocuteur",
        to_field_name="id",
    )
    alloc3pupil_hall2 = forms.ModelChoiceField(
        queryset=Person.objects.all(),
        widget=forms.Select,
        label="Sujet 3 élève",
        to_field_name="id",
    )
    alloc3inter_hall2 = forms.ModelChoiceField(
        queryset=Person.objects.all(),
        widget=forms.Select,
        label="Sujet 3 interlocuteur",
        to_field_name="id",
    )
    alloc4pupil_hall2 = forms.ModelChoiceField(
        queryset=Person.objects.all(),
        widget=forms.Select,
        label="Sujet 4 élève",
        to_field_name="id",
    )
    alloc4inter_hall2 = forms.ModelChoiceField(
        queryset=Person.objects.all(),
        widget=forms.Select,
        label="Sujet 4 interlocuteur",
        to_field_name="id",
    )
    alloc1pupil_hall3 = forms.ModelChoiceField(
        queryset=Person.objects.all(),
        widget=forms.Select,
        label="Sujet 1 élève",
        to_field_name="id",
    )
    alloc2pupil_hall3 = forms.ModelChoiceField(
        queryset=Person.objects.all(),
        widget=forms.Select,
        label="Sujet 2 élève",
        to_field_name="id",
    )
    vcm1 = forms.ModelChoiceField(
        queryset = Person.objects.exclude(cong_functions=""),
        widget=forms.Select,
        label="Sujet VCM 1",
        to_field_name="id",
    )
    vcm2 = forms.ModelChoiceField(
        queryset = Person.objects.exclude(cong_functions=""),
        widget=forms.Select,
        label="Sujet VCM 2",
        to_field_name="id",
    )
    vcm3 = forms.ModelChoiceField(
        queryset=Person.objects.filter(cong_functions__icontains="ancien"),
        widget=forms.Select,
        label="Sujet VCM 3",
        to_field_name="id",
    )
    vcm1_duration = forms.CharField(
        label="Durée sujet VCM 1", max_length=100, required=True
    )
    vcm2_duration = forms.CharField(
        label="Durée sujet VCM 2", max_length=100, required=False
    )
    vcm3_duration = forms.CharField(
        label="Durée sujet VCM 3", max_length=100, required=False
    )
    vcm1_title = forms.CharField(
        label="Titre sujet VCM 1", max_length=100, required=True
    )
    vcm2_title = forms.CharField(
        label="Titre sujet VCM 2", max_length=100, required=False
    )
    vcm3_title = forms.CharField(
        label="Titre sujet VCM 3", max_length=100, required=False
    )
    eba = forms.ModelChoiceField(
        queryset=Person.objects.filter(cong_functions__icontains="ancien"),
        widget=forms.Select,
        label="Etude biblique de l'assemblée",
        to_field_name="id",
    )
    eba_reader = forms.ModelChoiceField(
        queryset=Person.objects.filter(gender="MALE"),
        widget=forms.Select,
        label="Lecteur",
        to_field_name="id",
    )
    supervisor = forms.CharField(
        label="Responsable de circonscription",
    )
    special_speech = forms.CharField(
        label="Titre du discours spécial", max_length=100, required=False
    )

    parking = forms.ModelChoiceField(
        queryset=Person.objects.filter(gender="MALE"),
        widget=forms.Select,
        label="Parking",
        to_field_name="id",
    )
    entrance = forms.ModelChoiceField(
        queryset=Person.objects.filter(gender="MALE"),
        widget=forms.Select,
        label="Entrée",
        to_field_name="id",
    )
    inside = forms.ModelChoiceField(
        queryset=Person.objects.filter(gender="MALE"),
        widget=forms.Select,
        label="Auditorium",
        to_field_name="id",
    )
    podium = forms.ModelChoiceField(
        queryset=Person.objects.filter(gender="MALE"),
        widget=forms.Select,
        label="Estrade",
        to_field_name="id",
    )
    sono1 = forms.ModelChoiceField(
        queryset=Person.objects.filter(gender="MALE"),
        widget=forms.Select,
        label="Sono 1",
        to_field_name="id",
    )
    sono2 = forms.ModelChoiceField(
        queryset=Person.objects.filter(gender="MALE"),
        widget=forms.Select,
        label="Sono 2",
        to_field_name="id",
    )
    mic1 = forms.ModelChoiceField(
        queryset=Person.objects.filter(gender="MALE"),
        widget=forms.Select,
        label="Perche 1",
        to_field_name="id",
    )
    mic2 = forms.ModelChoiceField(
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
        self.fields["president"].label_from_instance = lambda obj: obj.fullname
        self.fields["prayer1"].label_from_instance = lambda obj: obj.fullname
        self.fields["prayer2"].label_from_instance = lambda obj: obj.fullname
        self.fields["jewels"].label_from_instance = lambda obj: obj.fullname
        self.fields["pearls"].label_from_instance = lambda obj: obj.fullname
        self.fields["reading1"].label_from_instance = lambda obj: obj.fullname
        self.fields["reading2"].label_from_instance = lambda obj: obj.fullname
        self.fields["reading3"].label_from_instance = lambda obj: obj.fullname
        self.fields["advisor2"].label_from_instance = lambda obj: obj.fullname
        self.fields["advisor3"].label_from_instance = lambda obj: obj.fullname
        self.fields["alloc1pupil_hall1"].label_from_instance = lambda obj: obj.fullname
        self.fields["alloc1inter_hall1"].label_from_instance = lambda obj: obj.fullname
        self.fields["alloc2pupil_hall1"].label_from_instance = lambda obj: obj.fullname
        self.fields["alloc2inter_hall1"].label_from_instance = lambda obj: obj.fullname
        self.fields["alloc3pupil_hall1"].label_from_instance = lambda obj: obj.fullname
        self.fields["alloc3inter_hall1"].label_from_instance = lambda obj: obj.fullname
        self.fields["alloc4pupil_hall1"].label_from_instance = lambda obj: obj.fullname
        self.fields["alloc4inter_hall1"].label_from_instance = lambda obj: obj.fullname
        self.fields["alloc1pupil_hall2"].label_from_instance = lambda obj: obj.fullname
        self.fields["alloc1inter_hall2"].label_from_instance = lambda obj: obj.fullname
        self.fields["alloc2pupil_hall2"].label_from_instance = lambda obj: obj.fullname
        self.fields["alloc2inter_hall2"].label_from_instance = lambda obj: obj.fullname
        self.fields["alloc3pupil_hall2"].label_from_instance = lambda obj: obj.fullname
        self.fields["alloc3inter_hall2"].label_from_instance = lambda obj: obj.fullname
        self.fields["alloc4pupil_hall2"].label_from_instance = lambda obj: obj.fullname
        self.fields["alloc4inter_hall2"].label_from_instance = lambda obj: obj.fullname
        self.fields["alloc1pupil_hall3"].label_from_instance = lambda obj: obj.fullname
        self.fields["alloc1pupil_hall3"].label_from_instance = lambda obj: obj.fullname
        self.fields["vcm1"].label_from_instance = lambda obj: obj.fullname
        self.fields["vcm2"].label_from_instance = lambda obj: obj.fullname
        self.fields["vcm3"].label_from_instance = lambda obj: obj.fullname
        self.fields["eba"].label_from_instance = lambda obj: obj.fullname
        self.fields["eba_reader"].label_from_instance = lambda obj: obj.fullname
        self.fields["parking"].label_from_instance = lambda obj: obj.fullname
        self.fields["entrance"].label_from_instance = lambda obj: obj.fullname
        self.fields["inside"].label_from_instance = lambda obj: obj.fullname
        self.fields["podium"].label_from_instance = lambda obj: obj.fullname
        self.fields["sono1"].label_from_instance = lambda obj: obj.fullname
        self.fields["sono2"].label_from_instance = lambda obj: obj.fullname
        self.fields["mic1"].label_from_instance = lambda obj: obj.fullname
        self.fields["mic2"].label_from_instance = lambda obj: obj.fullname


class WeekMeetingForm(forms.ModelForm):

    class Meta:
        model = Meeting
        fields = "__all__"
