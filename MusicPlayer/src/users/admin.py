from django.contrib import admin
from .models import User



class SuperUserFilter(admin.SimpleListFilter):
    title='Superuser'
    parameter_name = 'Superuser'
    def lookups(self, request, model_admin):
        return [('superuser','superuser')]
    def queryset(self, request, queryset):
        if self.value() == 'superuser':
            return queryset.filter(is_superuser =True)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username','first_name','last_name','phone','is_active','is_superuser']
    search_fields = ['phone','username']
    list_filter = [SuperUserFilter]
    list_editable = ['is_active']




