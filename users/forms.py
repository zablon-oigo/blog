from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class LoginForm(forms.Form):
    username=forms.CharField(max_length=65, widget=forms.TextInput(attrs={
        'placeholder':'Enter your username',
        'class':'w-full py-2 px-4 rounded-xl mb-2 '
    }))
    password=forms.CharField(max_length=65, widget=forms.PasswordInput(attrs={
        'placeholder':'Enter your password',
        'class':'w-full px-4 py-2 rounded-xl mb-2'
    }))
   
class RegForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2',]