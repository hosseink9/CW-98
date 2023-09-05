from django import forms
from django.forms import ModelForm
from .models import *

class UploadSongsForm(ModelForm):
    class Meta:
        model = Song
        fields = ('title','cover_photo','audio_file','artist','geners',)


class PlaylistForm(ModelForm):
    class Meta:
        model = Playlist
        fields = ('title','description','songs',)

class AddtoPlaylistForm(forms.Form):
    song_id=forms.CharField()
    playlist_id=forms.CharField()
