from django.shortcuts import render,redirect
from django.views.generic import FormView,CreateView
from django.urls import reverse_lazy

from .models import User
from .forms import *

class SignInView(CreateView):

    template_name = 'users/signin.html'
    form_class = UserSignin
    success_url = reverse_lazy("geners:song_list")

    def dispatch(self, request, *args, **kwargs):
        if isinstance(request.user, User):
            return redirect("geners:song_list")
        return super().dispatch(request, *args, **kwargs)