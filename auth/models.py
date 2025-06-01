from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.contrib.auth.base_user import BaseUserManager

class AuthUserManager(BaseUserManager):
  def create_user(self, email, password, **extra_fields):
    email = self.normalize_email(email)
    user = self.model(email=email, **extra_fields)
    user.set_password(password)
    user.save()
    return user

  def create_superuser(self, email, password, **extra_fields):
    extra_fields.update({
      'is_staff': True,
      'is_superuser': True,
      'is_active': True,
    })
    return self.create_user(email, password, **extra_fields)

class AuthUser(AbstractBaseUser, PermissionsMixin):
  objects = AuthUserManager()
  email = models.EmailField('email', primary_key=True, unique=True)
  is_staff = models.BooleanField('сотрудник', default=False) #useless. For django
  is_active = models.BooleanField('активный', default=True) #useless. For django
  date_joined = models.DateTimeField(default=timezone.now)

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = []
    
  class Meta:
    verbose_name = 'Пользователь'
    verbose_name_plural = 'Пользователи'