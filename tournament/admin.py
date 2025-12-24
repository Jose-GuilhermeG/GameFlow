from django.contrib import admin
from tournament.models import Tournament

# Register your models here.
@admin.register(Tournament)
class TournamentAdmin(admin.ModelAdmin):
    ...