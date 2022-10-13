from dataclasses import fields
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class SignUpUserForm(UserCreationForm):
    class Meta():
        model = User
        fields = ['username', 'email','first_name', 'last_name', 'password1', 'password2']


class LoginUserForm(AuthenticationForm):
    class Meta():
        fields = '__all__'

