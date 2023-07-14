from django.urls import path
from . import views

urlpatterns=[
    path("author/", views.all_author, name="all_author"),
    path("author/<int:pk>", views.author_details, name="author_details")
]