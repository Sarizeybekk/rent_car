from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

from .models import CustomUser
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']
# Giriş Formu
class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)