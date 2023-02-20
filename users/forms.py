from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    #Esta clase hereda de UserCreationForm, el cual de una manera muy sencilla elabora y presenta un 
    #formulario de registro de usuario, con seteos de seguridad para passwords.
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']