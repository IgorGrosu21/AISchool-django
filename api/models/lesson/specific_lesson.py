from django.db import models

from ..media import WithFiles

from .lesson import Lesson

class SpecificLesson(WithFiles):
  lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='specific_lessons', verbose_name='Урок')
  date = models.DateField('Дата')
  title = models.CharField('Тема урока', blank=True, max_length=128)
  desc = models.TextField('Домашнее задание', blank=True)
  links = models.TextField('Ссылки', blank=True)
  last_modified = models.DateTimeField('Время', auto_now=True)

  homeworks: models.Manager
  notes: models.Manager

  @property
  def students(self):
    return self.lesson.students

  @property
  def allowed_to_edit(self):
    return {self.lesson.teacher.user.id} | set(*self.lesson.klass.students.filter(is_manager=True).values_list('user__id')), True

  def __str__(self):
    return f'{self.lesson} {self.date}'

  class Meta:
    verbose_name = 'Конкретный урок'
    verbose_name_plural = 'Конкретные уроки'