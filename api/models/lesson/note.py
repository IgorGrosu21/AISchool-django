from django.db import models
from uuid import uuid4

from .specific_lesson import SpecificLesson
from ..person import Student

class Note(models.Model):
  id = models.UUIDField('id', default=uuid4, primary_key=True)
  note = models.SmallIntegerField('Оценка', default=10)
  specific_lesson = models.ForeignKey(SpecificLesson, on_delete=models.CASCADE, related_name='given_notes', verbose_name='Конкретный урок')
  student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, default=None, related_name='notes', verbose_name='Ученик')
  comment = models.CharField('Комментарий', max_length=256, blank=True, default='')
  timestamp = models.DateTimeField('Время', auto_created=True)
  
  def __str__(self):
    return f'{self.note} для {self.student} по {self.specific_lesson}'
  
  class Meta:
    verbose_name = 'Оценка'
    verbose_name_plural = 'Оценки'