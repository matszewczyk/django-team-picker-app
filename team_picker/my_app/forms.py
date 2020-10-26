from django import forms
from my_app.models import Player,Team,Membership

class PlayerForm(forms.ModelForm):

    class Meta():
        model = Player
        fields = ('name', 'surname')

class TeamForm(forms.ModelForm):

    class Meta():
        model = Team
        fields = ('name', 'members', 'password')

class MembershipForm(forms.ModelForm):
    password = forms.CharField(label='Password:')

    def __init__(self, *args, **kwargs):
        super(MembershipForm, self).__init__(*args, **kwargs)
        self.fields['player'].disabled = True

    class Meta():
        model = Membership
        fields = ('player', 'team', 'date_joined')
        widgets = {
            'date_joined': forms.HiddenInput()
        }

    # def save(self, commit=True):
    #     print(self.cleaned_data['password'])
    #     return super(MembershipForm, self).save(commit=commit)