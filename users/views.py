from django.views import generic
from users.forms import RegisterForm
from django.contrib.auth.views import LoginView as djangoLoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import login
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.
class LoginView(
    SuccessMessageMixin,
    djangoLoginView
):
    template_name = "users/login.html"
    success_message = _("Usuario logado com sucesso")
    
    
class RegisterView(
    SuccessMessageMixin,
    generic.FormView
):
    template_name = 'users/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy("users:profile")
    success_message = _("Usuario registrado com sucesso")
    
    def form_valid(self, form):
        user = form.save()
        login(self.request,user,'django.contrib.auth.backends.ModelBackend')
        return super().form_valid(form)
    
class ProfileView(
    LoginRequiredMixin,
    generic.TemplateView
):
    template_name = 'users/profile.html'
    extra_context = {"dont_use_header" : True}