from django.db import models
from uuid import uuid4

from ..school import Klass, Group
from ..subject import Subject
from ..person import Teacher
from .lesson_time import LessonTime

class Lesson(models.Model):
  id = models.UUIDField('id', default=uuid4, primary_key=True)
  klass = models.ForeignKey(Klass, on_delete=models.CASCADE, related_name='lessons', verbose_name='Класс')
  subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name='Предмет')
  lesson_time = models.ForeignKey(LessonTime, on_delete=models.CASCADE, related_name='lessons', verbose_name='Время')
  teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, related_name='lessons', null=True, verbose_name='Учитель')
  group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, related_name='lessons', verbose_name='Группа')
  
  specific_lessons: models.Manager
  
  def __str__(self):
    return f'{self.klass} {self.subject}, начало в {self.lesson_time.starting} ({self.lesson_time.weekday})'
  
  @property
  def manual_slug(self):
    return f'{self.subject.type.name}-{self.subject.lang}-{self.klass.grade}'
  
  @property
  def allowed_to_edit(self):
    return self.klass.allowed_to_edit
  
  @property
  def students(self):
    if self.group:
      return self.group.students
    return self.klass.students
  
  class Meta:
    verbose_name = 'Урок'
    verbose_name_plural = 'Уроки'