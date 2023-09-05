from typing import Any, Dict
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView,ListView,DetailView,CreateView
from geners.models import *
from .forms import *

class ListAllSongs(ListView):
    template_name = "index.html"
    model = Song
    context_object_name = 'song_list'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['playlists'] = Playlist.objects.filter(owner = self.request.user)
        context['playlistform'] = PlaylistForm()
        return context


class DesplaySongDetail(DetailView):
    model = Song
    template_name = 'song_detail.html'
    context_object_name = 'song'


class CreatePlaylist(CreateView):
    model = Playlist
    fields = ('title','description','songs')
    success_url = reverse_lazy('geners:song_list')

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        palylist = form.save(commit=False)
        palylist.owner = self.request.user
        palylist.save()
        return super().form_valid(form)