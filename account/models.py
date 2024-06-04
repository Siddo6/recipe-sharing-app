from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager

from django.contrib.auth.models import Group, Permission


# Create your models here.

class CustomUserManager (UserManager):
    def _create_user_ (self, name, email, password, **extra_fields):

        if not email :
            raise ValueError ('You should provide a valid email before continuing.')
        
        email=self.normalize_email(email)
        user=self.model(email=email, name=name, **extra_fields)
        user.set_password(password)
        user.save (using=self._db)

        return user
    
    def create_user(self, name, email, password, **extra_fields):

        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        return self._create_user_(name, email, password, **extra_fields)
    
    def create_superuser(self, name, email, password, **extra_fields):

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self._create_user_(name, email, password, **extra_fields)


class User (AbstractBaseUser, PermissionsMixin):

    id=models.AutoField(primary_key=True, auto_created=True, editable=False)
    email=models.EmailField(unique=True)
    name=models.CharField(max_length=150, blank=True, null=True)

    is_active=models.BooleanField(default=True)
    is_superuser=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)

    date_joined=models.DateTimeField(auto_now_add=True)
    last_login=models.DateTimeField(blank=True, null=True)

    objects=CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD='email'
    REQUIRED_FIELDS=['name']

    groups = models.ManyToManyField(Group, related_name='custom_user_set')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_set')
