from django.urls import path
from users import views
from allauth.socialaccount.providers.google.views import oauth2_login

urlpatterns = [
    path(
        'login/',
        views.LoginView.as_view(),
        name='login'
    ),
    path(
        'register/',
        views.RegisterView.as_view(),
        name='register'    
    ),
    path(
        'me/',
        views.ProfileView.as_view(),
        name='profile',    
    ),
    path("login/google/", oauth2_login, name="google_login"),
]
