from typing import Set, Tuple

from django.db import models

from auth.models import AuthUser

from ..country.city import City
from ..with_uuid import WithUUID

from .user_logic import UserLogic
from .user_routes import UserRoutes

class User(WithUUID, UserLogic, UserRoutes):
  account = models.OneToOneField(AuthUser, on_delete=models.CASCADE, unique=True, related_name='user')
  name = models.CharField('Имя', max_length=16)
  surname = models.CharField('Фамилия', max_length=16)
  city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, verbose_name='Город', related_name='users')
  lang = models.CharField('Язык', blank=True, max_length=2)
  avatar = models.ImageField('Аватар', blank=True, upload_to='avatars/')
  is_verified = models.BooleanField('Верифицированный', default=False)
  
  socials: models.Manager
  
  def __str__(self):
    return self.name + ' ' + self.surname if self.name else str(self.id)
  
  @property
  def allowed_to_edit(self) -> Tuple[Set[str], bool]:
    # First element: set of user IDs that can edit
    # Second element: boolean indicating if user needs to be verified
    return {self.id}, False
  
  class Meta:
    verbose_name = 'Пользователь'
    verbose_name_plural = 'Пользователи'