from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin, AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from .manager import UserManager
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class User(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    phone = models.IntegerField(unique=True, validators=[
                                MinValueValidator(1000000000), MaxValueValidator(9999999999)])
    is_agent = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email
    
