from django.urls import path
from .views import *

app_name = 'geners'

urlpatterns = [
    path('', ListAllSongs.as_view(), name='song_list'),
    path('song_detail/<int:pk>', DesplaySongDetail.as_view(), name='song_detail'),
    path('geners', ListAllGeners.as_view(), name='geners'),
    path('gener_songs/<int:pk>', ListAllGenerSongs.as_view(), name='gener_songs'),
    path('playlist/', PlaylistView.as_view(), name='playlist'),
    path('playlistsongs/<int:pk>', PlaylistSongsView.as_view(), name='playlistsongs'),
    path('add_to_playlist',AddSongView.as_view(),name='add_to_playlist')
]