from django import forms
from .generalFunctions import *
from .models import School, Season, Region, EventType, ScoreMapping, Account, Log

class SeasonForm(forms.ModelForm):
    class Meta:
        model = Season
        fields = '__all__'

class RegionForm(forms.ModelForm):
    class Meta:
        model = Region
        fields = '__all__'

class EventTypeForm(forms.ModelForm):
    class Meta:
        model = EventType
        fields = '__all__'

class ScoreMappingForm(forms.ModelForm):
    class Meta:
        model = ScoreMapping
        fields = '__all__'

class LogForm(forms.ModelForm):
    class Meta:
        model = Log
        fields = '__all__'

class AccountForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.data = kwargs.pop('data', None);
        self.field_data = (lambda x: x if x else {})(noneCatcher('field_data', self.data));
        self.choice_data = (lambda x: x if x else {})(noneCatcher('choice_data', self.data));
        for key, value in self.choice_data.items():
            self.fields[key] = forms.ChoiceField(choices=value);
        for key, value in self.field_data.items():
            self.fields[key].initial = value;

    account_type = forms.ChoiceField(choices=[]);
    account_email = forms.EmailField();
    account_password = forms.CharField(max_length=200);
    account_status = forms.ChoiceField(choices=[]);
    account_linked_id = forms.IntegerField(initial=-1);

class SchoolForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.data = kwargs.pop('data', None);
        self.field_data = (lambda x: x if x else {})(noneCatcher('field_data', self.data));
        self.choice_data = (lambda x: x if x else {})(noneCatcher('choice_data', self.data));
        for key, value in self.choice_data.items():
            self.fields[key] = forms.ChoiceField(choices=value);
        for key, value in self.field_data.items():
            self.fields[key].initial = value;

    school_name = forms.CharField(max_length=200);
    school_region = forms.ChoiceField(choices=[]);
    school_status = forms.ChoiceField(choices=[]);
    school_season_score = forms.FloatField(initial=0);
    account_email = forms.EmailField();
    account_password = forms.CharField(max_length=200);

class TeamForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.data = kwargs.pop('data', None);
        self.field_data = (lambda x: x if x else {})(noneCatcher('field_data', self.data));
        self.choice_data = (lambda x: x if x else {})(noneCatcher('choice_data', self.data));
        for key, value in self.choice_data.items():
            self.fields[key] = forms.ChoiceField(choices=value);
        for key, value in self.field_data.items():
            self.fields[key].initial = value;

    team_name = forms.CharField(max_length=200);
    team_school = forms.ChoiceField(choices=[]);
    team_status = forms.ChoiceField(choices=[]);

class MemberForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.data = kwargs.pop('data', None);
        self.field_data = (lambda x: x if x else {})(noneCatcher('field_data', self.data));
        self.choice_data = (lambda x: x if x else {})(noneCatcher('choice_data', self.data));
        for key, value in self.choice_data.items():
            self.fields[key] = forms.ChoiceField(choices=value);
        for key, value in self.field_data.items():
            self.fields[key].initial = value;

    member_name = forms.CharField(max_length=200);
    member_school = forms.ChoiceField(choices=[]);
    member_email = forms.EmailField();
    member_status = forms.ChoiceField(choices=[]);

class MemberGroupForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.data = kwargs.pop('data', None);
        self.field_data = (lambda x: x if x else {})(noneCatcher('field_data', self.data));
        self.choice_data = (lambda x: x if x else {})(noneCatcher('choice_data', self.data));
        for key, value in self.choice_data.items():
            self.fields[key] = forms.ChoiceField(choices=value);
        for key, value in self.field_data.items():
            self.fields[key].initial = value;
    member_group_name = forms.CharField(max_length=200);
    member_group_school = forms.ChoiceField(choices=[]);

class EventCreationForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.data = kwargs.pop('data', None);
        self.field_data = (lambda x: x if x else {})(noneCatcher('field_data', self.data));
        self.choice_data = (lambda x: x if x else {})(noneCatcher('choice_data', self.data));
        for key, value in self.choice_data.items():
            self.fields[key] = forms.ChoiceField(choices=value);
        for key, value in self.field_data.items():
            self.fields[key].initial = value;
    event_creation_event_type = forms.ChoiceField(choices=[]);
    event_creation_event_name = forms.CharField(max_length=200);
    event_creation_event_description = forms.CharField(max_length=1500);
    event_creation_event_location = forms.CharField(max_length=1000);
    event_creation_event_host = forms.ChoiceField(choices=[]);
    event_creation_event_team = forms.ChoiceField(choices=[]);
    event_creation_event_num_race = forms.IntegerField();
    event_creation_event_num_boat = forms.IntegerField();
    event_creation_event_start_date = forms.DateTimeField();
    event_creation_event_end_date = forms.DateTimeField();

