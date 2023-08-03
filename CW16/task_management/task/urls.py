from django.urls import path
from . import views

urlpatterns=[
    path("task/", views.all_task, name="all_task"),
    path("task/<int:pk>", views.task_details, name="task_details")
]