from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

USER = get_user_model()

class RegisterForm(
    forms.ModelForm
):
    
    email = forms.EmailField()
    
    class Meta:
        model = USER
        fields = ('username','nickname','email','password')
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if USER.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already in use.")
        return email
    
    def clean_username(self):
        username = self.cleaned_data.get("username")
        if USER.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already in use.")
        return username
    
    def save(self):
        data = self.cleaned_data
        password = data.pop("password")
        user = USER(**data)
        user.set_password(password)
        user.save()
        return user