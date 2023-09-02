from django.shortcuts import render
from django.views.generic import FormView,ListView
from geners.models import *


class ListAllSongs(ListView):
    template_name = "index.html"
    model = Song
    context_object_name = 'song_list'

