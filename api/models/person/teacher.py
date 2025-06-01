from django.db import models
from uuid import uuid4

from ..user import User
from ..subject import SubjectName

class Teacher(models.Model):
  id = models.UUIDField('id', default=uuid4, primary_key=True)
  user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher', verbose_name='Пользователь')
  subject_names = models.ManyToManyField(SubjectName, related_name='all_teachers', verbose_name='Предметы')
  experience = models.SmallIntegerField('Стаж работы', default=0)
  
  def __str__(self):
    return f'{self.user}'
  
  class Meta:
    verbose_name = 'Учитель'
    verbose_name_plural = 'Учителя'