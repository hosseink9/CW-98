from django.shortcuts import render
from .models import User
from .forms import UserForm,UserLoginForm

def userlogin(request):
    if request.method["POST"]:
        form=UserLoginForm(request.POST)
        if form.is_valid():
            clean_d=form.cleaned_data
            username=clean_d['username']
            password=clean_d['password']
    else:
        form=UserLoginForm()
        return render(request, 'login.html',{'form':form})
