from django.forms import ModelForm,PasswordInput,CharField, ValidationError
from django.contrib.auth.hashers import make_password,check_password
from django import forms
from .models import *

class UserSigninForm(ModelForm):
    confirm_password=CharField(widget=PasswordInput)
    password=CharField(max_length=30,widget=PasswordInput)
    class Meta:
        model=User
        fields=('username','first_name','last_name','phone','account','photo','password')

    def clean(self):
        cleaned_data = super(UserSigninForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise ValidationError("password and confirm_password does not match")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class UserLoginForm(forms.Form):
    phone=forms.CharField(
        validators = [phone_validator],
        widget = forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "Phone"
        }))
    password=CharField(max_length=30,widget=PasswordInput)

