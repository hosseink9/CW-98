from django.forms import ModelForm
from django import forms
from .models import *

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('text','song')
        # <input type="text" id="addANote" class="form-control" placeholder="Type comment..." />
        widgets = {'song': forms.TextInput(attrs={'type':'hidden'}),
                   'text': forms.TextInput(attrs={'class': 'form-control', 'id': 'addANote', 'placeholder': "Type comment..."})}