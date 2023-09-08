from django.urls import path
from .views import *

app_name = 'users'

urlpatterns = [
    path('signin', SignInView.as_view(), name='signin'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', logout_user,name='logout')
]