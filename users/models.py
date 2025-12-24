from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from core.constants import SHORT_CHAR_LENGTH

# Create your models here.
class User(
    AbstractUser
):
    nickname = models.CharField(
        verbose_name=_("Apelido"),
        null=False,
        blank=False,
        unique=False,
        max_length=SHORT_CHAR_LENGTH
    )
    
    photo = models.ImageField(
        verbose_name=_("Foto do usuario"),
        upload_to="users/photo/%Y/%m/",
        null=True,
        blank=False,
    )
    