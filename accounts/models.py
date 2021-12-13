from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import UserManager


class User(AbstractBaseUser):
    full_name = models.CharField(max_length=70)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    age = models.PositiveSmallIntegerField()
    email = models.EmailField(max_length=100)
    username = models.CharField(max_length=40, unique=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['full_name', 'age', 'email']
    objects = UserManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    class Meta:
        db_table = 'User'
        verbose_name = 'user'
        verbose_name_plural = 'users'
