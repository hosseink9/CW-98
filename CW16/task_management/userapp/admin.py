from django.contrib import admin
from .models import User
from task.models import Task


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["username", 'is_active',
                    'number_of_task', 'is_greate_user']

    @admin.display(ordering="username")
    def number_of_task(self, user):
        query = Task.objects.filter(user=user).count()
        return query

    def is_greate_user(self, user):
        query = Task.objects.filter(user=user).count()
        if query > 10:
            return True
        return False
