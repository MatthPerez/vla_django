from django import forms
from we.models import WeekendMeeting
from persons.models import Person


class AddWeekendMeeting(forms.Form):
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
    speaker = forms.ModelChoiceField(
        required=True,
        queryset=Person.objects.exclude(cong_functions=""),
        widget=forms.Select,
        label="Allocuteur",
        to_field_name="id",
    )
    speech_title = forms.CharField(
        required=False,
        label="titre du discours",
    )
    watchtower = forms.ModelChoiceField(
        required=True,
        queryset=Person.objects.filter(cong_functions__icontains="ancien"),
        widget=forms.Select,
        label="Tour de Garde",
        to_field_name="id",
    )
    watchtower_reader = forms.ModelChoiceField(
        required=True,
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

    def __init__(self, *args, **kwargs):
        super(AddWeekendMeeting, self).__init__(*args, **kwargs)

        fields_with_fullname = [
            "president",
            "prayer1",
            "prayer2",
            "speaker",
            "watchtower",
            "watchtower_reader",
        ]

        for field in fields_with_fullname:
            if field in self.fields:
                self.fields[field].label_from_instance = lambda obj: obj.fullname


class WeekMeetingForm(forms.ModelForm):

    class Meta:
        model = WeekendMeeting
        fields = "__all__"
        widgets = {
            "date": forms.DateInput(
                attrs={"type": "date", "placeholder": "AAAA-MM-JJ"}
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        optional_fields = [
            "watchtower_reader",
            "supervisor",
            "special_speech",
        ]
        for field in optional_fields:
            self.fields[field].required = False
            self.fields[field].widget.attrs.update({"required": False})

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["date"].input_formats = ["%Y-%m-%d"]
