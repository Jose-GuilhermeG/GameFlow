from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import get_user_model

USER = get_user_model()

class RegisterForm(
    UserCreationForm
):
    
    email = forms.EmailField()
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if USER.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already in use.")
        return email
    
    def save(self):
        data = self.cleaned_data
        password = data.pop("password1")
        data.pop("password2")
        user = USER(**data)
        user.set_password(password)
        user.save()
        return user