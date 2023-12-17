from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)


class UserManager(BaseUserManager):
    """custom user model manager"""
    def create_user(self, email, password,**extras):
        """create new user and return it"""
        if not email:
            raise ValueError("Email is required")
        
        if not password:
            raise ValueError("Password is required")
        
        user = self.model(email=self.normalize_email(email), **extras)

        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, password, **extras):
        """create superuser"""
        user = self.create_user(email, password, **extras)

        user.is_staff = True
        user.is_superuser = True
        user.is_active = True

        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    """custom user model for the project"""
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name']

    objects = UserManager()

    def __str__(self) -> str:
        return self.email