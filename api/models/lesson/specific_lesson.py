from django.db import models
from uuid import uuid4

from .lesson import Lesson

class SpecificLesson(models.Model):
  id = models.UUIDField('id', default=uuid4, primary_key=True)
  lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='specific_lessons', verbose_name='Урок')
  date = models.DateField('Дата')
  title = models.CharField('Тема урока', blank=True, max_length=128)
  desc = models.TextField('Домашнее задание', blank=True)
  links = models.TextField('Ссылки', blank=True)
  
  def __str__(self):
    return f'{self.lesson} {self.date}'
  
  @property
  def allowed_to_edit(self):
    return self.lesson.allowed_to_edit
  
  class Meta:
    verbose_name = 'Конкретный урок'
    verbose_name_plural = 'Конкретные уроки'