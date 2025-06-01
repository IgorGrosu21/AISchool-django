from django.db import models
from uuid import uuid4

from .specific_lesson import SpecificLesson
from ..person import Student

class Homework(models.Model):
  id = models.UUIDField('id', default=uuid4, primary_key=True)
  specific_lesson = models.ForeignKey(SpecificLesson, on_delete=models.CASCADE, related_name='uploaded_homeworks', verbose_name='Конкретный урок')
  student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='homeworks', verbose_name='Ученик')
  comment = models.CharField('Комментарий', max_length=256, blank=True, default='')
  
  def __str__(self):
    return f'{self.student} на {self.specific_lesson}'
  
  class Meta:
    verbose_name = 'Домашнее задание'
    verbose_name_plural = 'Домашние задания'