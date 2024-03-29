from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from apps.accounts.manager import UserManager



class CustomUser(AbstractBaseUser, PermissionsMixin):

    ROLE_CHOICES = (
        ('manager', 'Manager'),
        ('user', 'User'),
    )
    role = models.CharField(choices=ROLE_CHOICES, max_length=15, blank=True, null=True)
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),)
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."),)
    

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
        app_label = "accounts"


    def __str__(self):
        return f"{self.email}"