import django_filters as Filter 
from tournament.models import Tournament , TournamentStatus

class TournamentFilter(
    Filter.FilterSet
):
    
    status_options = TournamentStatus.choices
    
    class Meta:
        model = Tournament
        fields = ['name','status','max_enrrolment','current_stage']
