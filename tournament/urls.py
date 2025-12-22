from django.urls import path

from tournament import views

urlpatterns = [
    path(
        'create/',
        views.CreateTournamentView.as_view(),
        name="create-tournament"
    ),
    path(
        '',
        views.ListTournamentsView.as_view(),
        name="list-tournament"
    ),
]
