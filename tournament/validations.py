from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def even_number_validate(value : int):
    if value % 2 != 0:
        raise ValidationError(_("O numero deve ser par"))
    