from django.db import models
from uuid import uuid4

from .lesson import Lesson
from ..media import WithFiles

class SpecificLesson(WithFiles):
  id = models.UUIDField('id', default=uuid4, primary_key=True)
  lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='specific_lessons', verbose_name='Урок')
  date = models.DateField('Дата')
  title = models.CharField('Тема урока', blank=True, max_length=128)
  desc = models.TextField('Домашнее задание', blank=True)
  links = models.TextField('Ссылки', blank=True)
  
  homeworks: models.Manager
  notes: models.Manager
  
  def __str__(self):
    return f'{self.lesson} {self.date}'
  
  @property
  def students(self):
    return self.lesson.students
  
  @property
  def allowed_to_edit(self):
    return {self.lesson.teacher.user.id} | set(*self.lesson.klass.students.filter(is_manager=True).values_list('user__id')), True
  
  class Meta:
    verbose_name = 'Конкретный урок'
    verbose_name_plural = 'Конкретные уроки'