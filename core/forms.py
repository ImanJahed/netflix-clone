from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class SignUpForm(forms.Form):
    email = forms.EmailField()
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput, label='Password Confirmation')

    def clean_password2(self):
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']

        if password and password2 and password2 != password:
            raise ValidationError("Passwords didn't match.!")

        return password

    def clean_username(self):
        username = self.cleaned_data['username']
        user = User.objects.filter(username=username).exists()

        if len(username) < 3:
            raise ValidationError('Username Must be At least 4 character')

        if user:
            raise ValidationError("Username Taken")

        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email).exists()

        if user:
            raise ValidationError('Email already exists.')

        return email
