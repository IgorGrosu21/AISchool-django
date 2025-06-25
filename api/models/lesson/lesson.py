from django.db import models
from uuid import uuid4

from ..school import Klass
from ..subject import SubjectName
from ..person import Teacher
from .lesson_time import LessonTime

class Lesson(models.Model):
  id = models.UUIDField('id', default=uuid4, primary_key=True)
  klass = models.ForeignKey(Klass, on_delete=models.CASCADE, related_name='timetable', verbose_name='Класс')
  subject_name = models.ForeignKey(SubjectName, on_delete=models.CASCADE, verbose_name='Предмет')
  lesson_time = models.ForeignKey(LessonTime, on_delete=models.SET_NULL, null=True, related_name='lessons', verbose_name='Время')
  teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, verbose_name='Учитель')
  
  def __str__(self):
    return f'{self.klass} {self.subject_name}, начало в {self.lesson_time.starting} ({self.lesson_time.weekday})'
  
  @property
  def allowed_to_edit(self):
    klass_allowed_to_edit, _ = self.klass.allowed_to_edit
    return klass_allowed_to_edit | ({self.teacher.user.id} if self.teacher else set()), True
  
  class Meta:
    verbose_name = 'Урок'
    verbose_name_plural = 'Уроки'