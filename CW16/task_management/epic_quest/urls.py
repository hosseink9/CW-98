from django.urls import path
from . import views
from django.contrib import admin

admin.site.site_header='ramin'
urlpatterns=[
    path('', views.home, name='home'),
    path("view_all", views.view_all, name='view_all'),
    path("category/", views.all_category, name="all_category"),
    path("category/<int:pk>", views.category_details, name="category_details"),
    path("search/", views.search, name="search"),
    path("search/result", views.search_details, name="search_details")
]