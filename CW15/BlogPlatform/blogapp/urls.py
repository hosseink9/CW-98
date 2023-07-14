from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name='home'),
    path("posts/", views.all_post, name="all_post"),
    path("posts/<int:pk>/", views.post_details, name="post_details"),
    path("category/", views.all_category, name="all_category"),
    path("author/", views.all_author, name="all_category")
]