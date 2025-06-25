from django.db import models
from uuid import uuid4

from auth.models import AuthUser
from ..country import City

class User(models.Model):
  id = models.UUIDField('id', default=uuid4, primary_key=True)
  account = models.OneToOneField(AuthUser, on_delete=models.CASCADE, unique=True, related_name='user')
  name = models.CharField('Имя', max_length=16)
  surname = models.CharField('Фамилия', max_length=16)
  city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, verbose_name='Город', related_name='users')
  lang = models.CharField('Язык', blank=True, max_length=2)
  avatar = models.ImageField('Аватар', blank=True, upload_to='avatars/')
  is_verified = models.BooleanField('Верифицированный', default=False)
  
  def __str__(self):
    return self.name + ' ' + self.surname if self.name else str(self.id)
  
  @property
  def student(self):
    return self.student_account if hasattr(self, 'student_account') else None
  
  @property
  def teacher(self):
    return self.teacher_account if hasattr(self, 'teacher_account') else None
  
  @property
  def is_teacher(self):
    return self.teacher != None
  
  @property
  def is_student(self):
    return self.student != None
  
  @property
  def allowed_to_edit(self):
    return {self.id}, False
  
  class Meta:
    verbose_name = 'Пользователь'
    verbose_name_plural = 'Пользователи'