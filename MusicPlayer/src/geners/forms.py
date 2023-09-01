from django.forms import ModelForm
from .models import *

class UploadSongsForm(ModelForm):
    class Meta:
        model = Song
        fields = ('title','upload_date','cover_photo','audio_file','artist','geners',)


class PlaylistForm(ModelForm):
    class Meta:
        model = Playlist
        fields = ('title','description','owner','songs',)
