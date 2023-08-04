from django import forms
from django.forms import ModelForm
from .models import *
from task.models import *

class CategoryForm(ModelForm):
    class Meta:
        model=Category
        fields=('name','description')

class TagForm(ModelForm):
    class Meta:
        model=Tag
        fields=('name',)
