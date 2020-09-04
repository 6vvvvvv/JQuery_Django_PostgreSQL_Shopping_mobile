from django import forms
from ..models import User

class LoginForm(forms.Form):
    username = forms.CharField(max_length=20, min_length=6, required=True, error_messages={
                               "required": 'username can not be empty', 'invalid': 'format error'},
                               widget=forms.TextInput(attrs={'class': 'user'}))
    passwd = forms.CharField(max_length=20, min_length=6,
                             widget=forms.PasswordInput)

# class registerForm(forms.Form):
