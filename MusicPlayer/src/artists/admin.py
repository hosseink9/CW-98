from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import Artist
from geners.models import Song


# admin.site.register(Artist)

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ['name','view_songs','bio','created_at','updated_at']
    ordering = ['name']
    search_fields = ['created_at',"name"]

    def view_songs(self, obj):
        url = reverse(f'admin:{Song._meta.app_label}_{Song._meta.model_name}_changelist')
        link = f'<a href="{url}?artist__id__exact={obj.pk}">View Songs</a>'
        return format_html(link)
    view_songs.short_description = 'Songs'
    readonly_fields = ('view_songs',)

