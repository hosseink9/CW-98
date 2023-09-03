from typing import Any, Dict
from django.shortcuts import render,redirect
from django.views.generic import FormView,CreateView
from django.urls import reverse_lazy
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import PBKDF2PasswordHasher

from .auth import UserAuthBackend
from .models import User
from .forms import *

class SignInView(CreateView):

    template_name = 'users/signin.html'
    form_class = UserSigninForm
    success_url = reverse_lazy("geners:song_list")

    def dispatch(self, request, *args, **kwargs):
        if isinstance(request.user, User):
            return redirect("geners:song_list")
        return super().dispatch(request, *args, **kwargs)


class LoginView(FormView):

    template_name = 'users/login.html'
    form_class = UserLoginForm
    success_url = reverse_lazy("geners:song_list")

    def dispatch(self, request, *args, **kwargs):
        if isinstance(request.user, User):
            return redirect("geners:song_list")
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        cd = form.cleaned_data
        phone = str(cd['phone'])
        password =cd['password']
        print(password)
        user = User.objects.filter(phone=phone).first()
        if user:
            print(user.check_password(password))
            if user.check_password(password):
                login(self.request,user,'users.auth.UserAuthBackend')
                return super().form_valid(form)
            else:
                form.add_error("password", "Password incorrect")
            return super().form_invalid(form)
        else:
            form.add_error("phone", "Phone number not found")
            return super().form_invalid(form)


@login_required
def logout_user(request):
    logout(request)
    return redirect("users:login")
