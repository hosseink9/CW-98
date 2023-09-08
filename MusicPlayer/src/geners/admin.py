from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import *

# admin.site.register(Song)
@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['title','view_artist','geners','upload_date']
    search_fields = ['title']
    ordering = ['title']


    # def get_artist(self, instance):
    #     return [artist.name for artist in instance.artist.all()]
    # get_artist.short_description = 'artist'

    def view_artist(self, obj):
        artist = [artist.name for artist in obj.artist.all()]
        url = reverse(f'admin:{Artist._meta.app_label}_{Artist._meta.model_name}_changelist')
        link = f'<a href="{url}?song__id__exact={obj.pk}">{",".join(artist)}</a>'
        return format_html(link)
    view_artist.short_description = 'artist'
    readonly_fields = ('view_artist',)


@admin.register(Gener)
class GenerAdmin(admin.ModelAdmin):

    list_display = ['name','view_songs']

    def view_songs(self, obj):
        url = reverse(f'admin:{Song._meta.app_label}_{Song._meta.model_name}_changelist')
        link = f'<a href="{url}?geners__id__exact={obj.pk}">View Songs</a>'
        return format_html(link)
    view_songs.short_description = 'Songs'
    readonly_fields = ('view_songs',)


@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ['title','description','owner','view_songs']

    def view_songs(self, obj):
        url = reverse(f'admin:{Song._meta.app_label}_{Song._meta.model_name}_changelist')
        link = f'<a href="{url}?playlist__id__exact={obj.pk}">View Songs</a>'
        return format_html(link)
    view_songs.short_description = 'Songs'
    readonly_fields = ('view_songs',)
