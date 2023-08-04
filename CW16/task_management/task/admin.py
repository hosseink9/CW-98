from django.contrib import admin
from .models import *
from django.contrib.sessions.models import Session

admin.site.register(Task)

 
class SessionAdmin(admin.ModelAdmin):
    def sessiondata(self, obj):
        return obj.get_decoded()
    
    list_display=['session_key','sessiondata']

admin.site.register(Session,SessionAdmin)
