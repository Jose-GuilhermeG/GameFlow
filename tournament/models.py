from django.db import models
from core.models import BaseModel
from django.utils.translation import gettext_lazy as _
from core.constants import SHORT_CHAR_LENGTH
from tournament.enums import TournamentStatus
from tournament.validations import even_number_validate
from django.core.validators import MinValueValidator , MaxValueValidator
from django.contrib.auth import get_user_model

USER = get_user_model()

# Create your models here.
class Tournament(
    BaseModel
):
    name = models.CharField(
        verbose_name=_("Nome do torneio"),
        max_length=SHORT_CHAR_LENGTH,
        null=False,
        blank=False,
        unique=True
    )
    
    description = models.TextField(
        verbose_name=_("Descrição do torneio"),
        null=True,
        blank=True
    )
    
    status = models.CharField(
        verbose_name=_("Status do torneio"),
        max_length=1,
        choices=TournamentStatus.choices,
        default=TournamentStatus.UNSTARTED,
        null=False,
        blank=False
    )
    
    max_enrrolment = models.IntegerField(
        verbose_name=_("Maximo de inscrições"),
        validators=[
            even_number_validate,
            MinValueValidator(4),
            MaxValueValidator(16)
        ],
        null=False,
        blank=False
    )
    
    owner = models.ForeignKey(
        verbose_name=_("Dono do torneio"),
        to=USER,
        on_delete=models.SET_NULL,
        related_name='tournaments',
        blank=False,
        null=True
    )
    
    current_stage = models.IntegerField(
        verbose_name=_("Etapa atual"),
        null=True,
        blank=False,
        default=0
    )
    
    def __str__(self):
        return self.name
    
    def get_total_stages(self):
        return int(self.max_enrrolment / 2)
    
    class Meta:
        verbose_name = _("Torneio")
        verbose_name_plural = _("Torneios")