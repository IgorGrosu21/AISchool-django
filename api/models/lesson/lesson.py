from django.db import models

from ..person.teacher import Teacher
from ..school.group import Group
from ..school.klass import Klass
from ..subject.subject import Subject
from ..with_uuid import WithUUID

from .lesson_time import LessonTime

class Lesson(WithUUID):
  klass = models.ForeignKey(Klass, on_delete=models.CASCADE, related_name='lessons', verbose_name='Класс')
  subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name='Предмет')
  lesson_time = models.ForeignKey(LessonTime, on_delete=models.CASCADE, related_name='lessons', verbose_name='Время')
  teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, related_name='lessons', null=True, verbose_name='Учитель')
  group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, related_name='lessons', verbose_name='Группа')

  specific_lessons: models.Manager

  @property
  def klass_slug(self) -> str:
    return self.klass.slug

  @property
  def manual_slug(self) -> str:
    return f'{self.subject.type.name}-{self.subject.lang}-{self.klass.grade}'

  @property
  def students(self):
    if self.group:
      return self.group.students
    return self.klass.students

  @property
  def allowed_to_edit(self):
    return self.klass.allowed_to_edit

  def __str__(self):
    return f'{self.klass} {self.subject}, начало в {self.lesson_time.starting} ({self.lesson_time.weekday})'

  class Meta:
    ordering = ['klass__school', 'klass', 'lesson_time__weekday', 'lesson_time__order']
    verbose_name = 'Урок'
    verbose_name_plural = 'Уроки'