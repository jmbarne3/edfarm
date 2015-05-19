from django import forms
from django.contrib.auth import authenticate, login

class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)
