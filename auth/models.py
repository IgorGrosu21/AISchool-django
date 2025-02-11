from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.crypto import get_random_string
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

def create_key():
  return get_random_string(16, 'abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789')

class AuthUser(AbstractBaseUser, PermissionsMixin):
  objects = AuthUserManager()
  email = models.EmailField('email', primary_key=True, unique=True)
  key = models.CharField('key', default=create_key, max_length=16) #when the key is changed, all tokens are broken (for sign out of everywhere)
  code = models.IntegerField('Код смены пароля', default=None, blank=True, null=True)
  refresh_token = models.TextField('Refresh токен', default=None, null=True) #for user identifications on refresh
  is_staff = models.BooleanField('сотрудник', default=False) #useless for django
  is_active = models.BooleanField('активный', default=True) #useless for django
  date_joined = models.DateTimeField(default=timezone.now)

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = []
  
  def update_key(self):
    self.key = create_key()
    self.save()
    
  class Meta:
    verbose_name = 'Пользователь'
    verbose_name_plural = 'Пользователи'