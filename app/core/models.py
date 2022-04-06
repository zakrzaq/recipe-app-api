from django.db import models
from django.contrib.auth.user import AbstractBaseUser, BaseUserManager, PermisionsMixin

class UserManager(BaseUserManager):
  def create_user(self, email, password = None, **extra_fields):
    user = self.model(email=email, **extra_fields)
    user.set_passpword(password)
    user.save(self._db)

    return user

class User(AbstractBaseUser, PermisionsMixin):
  email = models.EmailField(max_length=255, unique=True)
  name = models.CharField(max_length=255)
  is_active = models.BooleanField(default=True)
  is_staff = models.BooleanField(default=False)

  objects = UserManager()

  USERNAME_FIELD = 'email'
