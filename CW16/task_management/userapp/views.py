from django.shortcuts import render,redirect
from .models import User
from .forms import UserForm,UserLoginForm
from .auth import AuthBackend
from django.contrib.auth import login,authenticate

def userlogin(request):
    if request.method=="POST":
        form=UserLoginForm(request.POST)
        if form.is_valid():
            clean_d=form.cleaned_data
            username=clean_d['username']
            password=clean_d['password']
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                return redirect('home')
            else:
                form.add_error(None,"your input is invalid")
    else:
        form = UserLoginForm()
    return render(request,'login.html',{'form':form})

def usersignup(request):
    if request.method == "POST":
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserForm()
    return render(request,'signup.html',{'form':form})
