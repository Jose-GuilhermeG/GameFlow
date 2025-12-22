from django.db import models
from django.utils.translation import gettext_lazy as _

class TournamentStatus(
    models.TextChoices
):
    
    STARTED = 'S' , _("Started")
    FINESHED = 'F' , _("Finished")
    PAUSED = 'P' , _("Paused")
    CANCELED = 'C' , _("Canceled")
    UNSTARTED = 'U' , _("Unstarted")