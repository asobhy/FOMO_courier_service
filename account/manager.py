from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _



class UserManager(BaseUserManager):
    def create_user(self, email, phone, password, is_customer, is_agent, **extra_fields):
        if not email:
            raise ValueError("User must have an email")

        user = self.model(
            email=self.normalize_email(email),
            **extra_fields
        )

        user.is_customer = is_customer
        user.is_agent = is_agent
        user.set_password(password)  # change password to hash
        user.phone = phone
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        if not email:
            raise ValueError("User must have an email")

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_customer', False)
        extra_fields.setdefault('phone', 1111111111)

        user = self.model(
            email=self.normalize_email(email),
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
