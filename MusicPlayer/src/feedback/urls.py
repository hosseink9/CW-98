from django.urls import path
from .views import *

app_name = 'feedback'

urlpatterns = [
    path('add_like',LikeView.as_view(),name='add_like'),
    path('add_comment',CommentView.as_view(),name='add_comment')
]