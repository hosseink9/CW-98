from typing import Any, Dict
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import FormView,ListView,DetailView,CreateView,View
from geners.models import *
from .forms import *
from feedback.models import *
from feedback.forms import *
from django.contrib.auth.mixins import LoginRequiredMixin

class ListAllSongs(ListView):
    template_name = "index.html"
    model = Song
    context_object_name = 'song_list'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['playlists'] = Playlist.objects.filter(owner = self.request.user) if self.request.user.is_authenticated else []
        context['playlistform'] = PlaylistForm()
        return context

class ListAllGeners(ListView):
    template_name = "geners/geners.html"
    model = Gener
    context_object_name = 'geners'


class ListAllGenerSongs(DetailView):
    template_name = 'geners/gener_songs.html'
    model = Gener
    # context_object_name = "gener_songs"


class DesplaySongDetail(DetailView):
    model = Song
    template_name = 'geners/song_detail.html'
    context_object_name = 'song'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm(initial={'song': self.get_object().id})
        context['comments'] = Comment.objects.filter(song=self.get_object().id)
        context['playlists'] = Playlist.objects.filter(owner=self.request.user)
        return context



class CreatePlaylist(CreateView):
    template_name = 'geners/playlist.html'
    model = Playlist
    fields = ('title','description','songs')
    success_url = reverse_lazy('geners:song_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['playlists'] = Playlist.objects.filter(owner = self.request.user) if self.request.user.is_authenticated else []
        context['playlistform'] = PlaylistForm()
        return context


    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        palylist = form.save(commit=False)
        palylist.owner = self.request.user
        palylist.save()
        return super().form_valid(form)


class PlaylistView(ListView):
    template_name = 'geners/playlist.html'
    model = Playlist
    context_object_name = 'playlists'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['playlists'] = Playlist.objects.filter(owner = self.request.user) if self.request.user.is_authenticated else []
        context['playlistform'] = PlaylistForm()
        return context


class PlaylistSongsView(DetailView):
    template_name = 'geners/playlistsongs.html'
    model = Playlist
    context_object_name = 'playlist'

class AddSongView(LoginRequiredMixin,View):
    form_class = AddtoPlaylistForm

    def post(self, request):
        form=self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            playlist = Playlist.objects.get(id=cd['playlist_id'])
            song=Song.objects.get(id=cd['song_id'])
            playlist.songs.add(song)
            messages.success(request,'Song added successfully', 'success')
            return redirect('geners:song_detail',song.id)
        return redirect('geners:song_detail',song.id)


