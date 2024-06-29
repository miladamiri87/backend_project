from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.db import models

from accounts.manager import UserManager


class User(AbstractBaseUser):
    phone_number = models.CharField(max_length=11, unique=True)
    email = models.EmailField(unique=True, max_length=255)
    f_name = models.CharField(max_length=255, null=True)
    l_name = models.CharField(max_length=255, null=True)
    address = models.TextField(null=True)
    address_city = models.CharField(max_length=255, null=True)
    address_street = models.CharField(max_length=255, null=True)

    date_birthday = models.DateField(null=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.phone_number

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def is_staff(self):
        return self.is_admin

    @property
    def full_name(self):
        if self.f_name and self.l_name:
            return f'{self.f_name} {self.l_name}'

        return 'Unknown account'


class Otp(models.Model):
    phone_number = models.CharField(max_length=11)
    code = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.phone_number
