from django.forms import ModelForm,PasswordInput,CharField, ValidationError
from models import *

class UserForm(ModelForm):
    confirm_password=CharField(widget=PasswordInput)
    class Meta:
        model=User
        fields=('username','password','email')

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise ValidationError("password and confirm_password does not match")