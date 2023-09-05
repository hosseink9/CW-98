from django.urls import path
from .views import *

app_name = 'geners'

urlpatterns = [
    path('', ListAllSongs.as_view(), name='song_list'),
    path('song_detail/<int:pk>', DesplaySongDetail.as_view(), name='song_detail'),
    path('createplaylist', CreatePlaylist.as_view(), name='createplaylist')
]