from django import forms
from .models import Team, Member


class TeamRegistrationForm(forms.Form):
    team_name = forms.CharField(label='نام تیم', max_length=100)

    def clean_team_name(self):
        name = self.cleaned_data['team_name']
        if Team.objects.filter(name=name).exists():
            raise forms.ValidationError('این نام تیم قبلاً ثبت شده است.')
        return name
