from django.db import models
from uuid import uuid4

from auth.models import AuthUser
from ..country import City

class User(models.Model):
  id = models.UUIDField('id', default=uuid4, primary_key=True)
  account = models.OneToOneField(AuthUser, on_delete=models.CASCADE, unique=True, related_name='user')
  is_teacher = models.BooleanField('Учитель', default=False)
  name = models.CharField('Имя', max_length=16)
  surname = models.CharField('Фамилия', max_length=16)
  city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, verbose_name='Город', related_name='users')
  lang = models.CharField('Язык', blank=True, max_length=2)
  avatar = models.ImageField('Аватар', blank=True, upload_to='avatars/')
  
  def __str__(self):
    return self.name + ' ' + self.surname if self.name else str(self.id)
  
  @property
  def student(self):
    return self.student if hasattr(self, 'student') else None
  
  @property
  def teacher(self):
    return self.teacher if hasattr(self, 'teacher') else None
  
  @property
  def allowed_to_edit(self):
    return [self.id]
  
  class Meta:
    verbose_name = 'Пользователь'
    verbose_name_plural = 'Пользователи'