from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.db import models
from django.contrib.auth.models import User
from django import forms


class Register(UserCreationForm):
    email = forms.EmailField()
    fields = [
        'username', 'email', 'password', 'password_2'
    ]