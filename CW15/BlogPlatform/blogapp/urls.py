from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name='home'),
    path("posts/", views.all_post, name="all_post")
]