from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin
)
from django.utils.translation import ugettext_lazy as _

from apps.user.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom User model.
    """

    first_name = models.CharField(_('First name'), max_length=50,
                                  blank=True, null=True)
    last_name = models.CharField(_('Last name'), max_length=50,
                                 blank=True, null=True)
    email = models.EmailField(_('Email'), unique=True)
    date_joined = models.DateTimeField(_('Date joined'), auto_now_add=True)
    is_staff = models.BooleanField(_('Is staff'), default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_short_name(self):
        return self.first_name

    def get_full_name(self):
        if all([self.first_name, self.last_name]):
            return '{0} {1}'.format(self.first_name, self.last_name)
        else:
            return self.email

    def __str__(self):
        return self.get_full_name()
