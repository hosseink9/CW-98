from django.urls import path
from .views import *

app_name = 'geners'

urlpatterns = [
    path('song_list', ListAllSongs.as_view(), name='song_list')
]