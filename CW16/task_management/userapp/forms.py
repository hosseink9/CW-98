from django.forms import ModelForm,PasswordInput,CharField
from models import *

class UserForm(ModelForm):
    passwordinput=CharField(widget=PasswordInput)
    class Meta:
        model=User
        fields=('username','password','email')
