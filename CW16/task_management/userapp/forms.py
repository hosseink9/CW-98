from django.forms import ModelForm,PasswordInput,CharField, ValidationError
from django.contrib.auth.hashers import make_password
from django import forms
from .models import *

class UserForm(ModelForm):
    confirm_password=CharField(widget=PasswordInput)
    password=CharField(max_length=30,widget=PasswordInput)
    class Meta:
        model=User
        fields=('username','email','password')

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise ValidationError("password and confirm_password does not match")
        cleaned_data['password']=make_password('password')
        return cleaned_data
    
class UserLoginForm(forms.Form):
    username=forms.CharField(max_length=30)
    password=forms.CharField(max_length=30,widget=PasswordInput)
