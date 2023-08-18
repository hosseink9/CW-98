from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.utils.html import mark_safe


class CustomUserManager(BaseUserManager):
    # def create_user(self, email, username, first_name, last_name, photo, password=None):
    # if not email:
    #     raise ValueError("Users must have an email address")
    # email = self.normalize_email(email)
    # user = self.model(email=email, username=username, first_name=first_name, last_name=last_name, photo=photo)
    def create_user(self, username, password):
        user = self.model(username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(username, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    photo = models.ImageField(
        upload_to='profile_photos/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)
    objects = CustomUserManager()
    USERNAME_FIELD = 'username'

    def img_preview(self):
        return mark_safe(f'<img src = "{self.photo.url}" width = "300"/>')
