from django import forms
from tournament.models import Tournament

class TournamentCreateForm(
    forms.ModelForm
):
    class Meta:
        model = Tournament
        fields = ('name','description','max_enrrolment')