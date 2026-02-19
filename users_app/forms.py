from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    
    email = forms.EmailField() 
   # password1 = forms.CharField(widget=forms.PasswordInput, label='Password')
   # password2 = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')
    #username = forms.CharField(widget=forms.TextInput, label='Username')
    firstname = forms.CharField()
    lastname = forms.CharField()
    class Meta:
        model = User
        fields = ['username', 'firstname', 'lastname','email', 'password1', 'password2']