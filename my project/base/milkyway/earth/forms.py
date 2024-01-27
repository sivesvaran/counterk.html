from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

class UserForm(forms.ModelForm):
    model = UserProfile
    
    fields = ('name','first_name','last_name','email')

