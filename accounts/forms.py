from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
