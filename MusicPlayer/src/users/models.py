from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.exceptions import ValidationError
from main.models import BaseModel

import re





PHONE_REGEX_PATTERN = r"(((\+|00)(98))|0)?(?P<operator>9\d{2})-?(?P<middle3>\d{3})-?(?P<last4>\d{4})"

def phone_validator(phone:str):
    if not (matched := re.fullmatch(PHONE_REGEX_PATTERN, phone.strip())):
        raise ValidationError("Invalid phone number")
    return matched



class UserManager(BaseUserManager):

    def create_user(self, phone, password, **other_fields):
        if phone is None:
            raise ValueError("Phone not given")

        user = self.model(phone=phone, **other_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password=None, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(phone, password, **other_fields)


class PhoneNumberField(models.CharField):
    def get_prep_value(self, value):
        if value is None:
            return value

        try:
            regex = phone_validator(value)
        except ValidationError:
            raise

        phone_parts = regex.groupdict()
        phone = phone_parts["operator"]+phone_parts["middle3"]+phone_parts["last4"]
        return phone


class User(AbstractUser, BaseModel):
    Normal='Normal'
    Premium='Premium'
    CHOICES = [
        ('N',Normal),
        ('P',Premium)
    ]

    phone = PhoneNumberField(validators=[phone_validator], unique=True, max_length=20)

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='images/users', blank=True ,null=True)

    is_active = models.BooleanField(default=True)

    account = models.CharField(max_length=50, choices=CHOICES)

    objects = UserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.phone}"

