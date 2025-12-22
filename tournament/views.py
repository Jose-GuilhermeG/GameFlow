from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from tournament.forms import TournamentCreateForm
from django.utils.translation import gettext_lazy as _
from tournament.models import Tournament
from tournament.filters import TournamentFilter
from django_filters.views import FilterView
from django.urls import reverse_lazy

# Create your views here.
class CreateTournamentView(
    LoginRequiredMixin,
    SuccessMessageMixin,
    generic.CreateView,
):
    template_name = 'tournament/create_tournament.html'
    form_class = TournamentCreateForm
    success_url = reverse_lazy("tournament:list-tournament")
    success_message = _("Torneio criado com sucesso")
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.current_stage = 0
        form.save()
        return super().form_valid(form)
    
class ListTournamentsView(
    FilterView
):
    template_name ='tournament/list_tournament.html'
    queryset = Tournament.objects.all()
    context_object_name = 'tournaments'
    paginate_by = 10
    filterset_class = TournamentFilter