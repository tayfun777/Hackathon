from django import forms
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput)
    username = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)
