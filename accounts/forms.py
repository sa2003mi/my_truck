from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from . import models





class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=255 , required=True , widget= forms.EmailInput(),help_text='Email like is Example@gmail.com')
    class Meta:
        model = User 
        fields = ('username' ,'email','password1','password2')


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username', 'first_name', 'last_name', 'email'
        ]

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'image' , 'city' , 'bio'
        ]
