from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from allauth.socialaccount.providers.google.views import oauth2_callback
from allauth.socialaccount.views import login_cancelled

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/',include(('users.urls','users'),namespace='users')),
    path('tournaments/',include(('tournament.urls','tournament'),namespace='tournament')),
]

urlpatterns += [
    path("account/login/google/callback/", oauth2_callback, name="google_callback"),
    path("account/login/google/canceled", login_cancelled, name="socialaccount_login_cancelled"),
    path("__reload__/", include("django_browser_reload.urls")),
]

if settings.DEBUG :
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root = settings.MEDIA_ROOT
    )