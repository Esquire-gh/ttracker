from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifier
    for authentication.
    """
    def create_user(self, first_name, last_name, username=None, email=None, password=None, **extra_fields):
        """
        Create and save a User.
        """
        if not email:
            raise ValueError(_('Email is required!'))

        email = self.normalize_email(email)
        user = self.model(first_name=first_name, username=username, last_name=last_name, email=email, **extra_fields)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, first_name, last_name, email, username=None, password=None, **extra_fields):
        """
        Create and save a SuperUser.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self.create_user(first_name, last_name, username, email, password, **extra_fields)
