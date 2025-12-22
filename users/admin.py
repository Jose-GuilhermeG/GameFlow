from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as baseUserAdmin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

USER = get_user_model()

# Register your models here.
@admin.register(USER)
class UserAdmin(baseUserAdmin):
     fieldsets = (
        ("user infos", {"fields": ("username", "nickname","photo","password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )