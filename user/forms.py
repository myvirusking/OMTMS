from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from random import choice

class RegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Optional'}
    ), required=False)

    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Optional'}
    ), required=False)

    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control'}
    ))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control'}
    ))
    password2 = forms.CharField(label='Confirmed Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control'}
    ))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email',
                  'password1', 'password2']
        
