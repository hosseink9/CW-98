from django.urls import path
from .views import userlogin,usersignup

urlpatterns=[
    path("login/", userlogin, name="userlogin"),
    path("signup/", usersignup,name='usersignup')
]