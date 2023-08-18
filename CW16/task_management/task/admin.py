from django.contrib import admin
from . import models
from django.contrib.sessions.models import Session


@admin.register(models.Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'due_date', 'status_fields', 'category']
    readonly_fields = ["created_at", "updated_at"]
    list_editable = ['status_fields']
    ordering = ['title', 'status_fields']
    # list_select_related=['category']
    list_per_page = 4


class SessionAdmin(admin.ModelAdmin):
    def sessiondata(self, obj):
        return obj.get_decoded()

    list_display = ['session_key', 'sessiondata']


admin.site.register(Session, SessionAdmin)
