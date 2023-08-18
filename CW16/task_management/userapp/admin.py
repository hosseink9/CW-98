from django.contrib import admin
from .models import User
from task.models import Task


class AdminFilter(admin.SimpleListFilter):
    title = "Is_greate_user"
    parameter_name = "greate"

    def lookups(self, request, model_admin):
        return [('greate', 'Is_greate_user')]

    def queryset(self, request, queryset):
        if self.value() == 'greate':
            return queryset.filter(is_greate_user=True)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["username", 'is_active',
                    'number_of_task', 'is_greate_user']
    list_filter = [AdminFilter]

    @admin.display(ordering="username")
    def number_of_task(self, user):
        query = Task.objects.filter(user=user).count()
        return query

    def is_greate_user(self, user):
        query = Task.objects.filter(user=user).count()
        if query > 10:
            return True
        return False
    is_greate_user.boolean = True
