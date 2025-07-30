from django.db import models
from uuid import uuid4

from .specific_lesson import SpecificLesson
from ..person import Student

class Note(models.Model):
  VALUES = {
    'ma': 'Уважительный пропуск',
    'ua': 'Неуважительный пропуск',
    'da': 'Пропуск по болезни',
    '1': '1',
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9',
    '10': '10'
  }
  
  id = models.UUIDField('id', default=uuid4, primary_key=True)
  value = models.CharField('Значение', choices=VALUES, max_length=2)
  specific_lesson = models.ForeignKey(SpecificLesson, on_delete=models.CASCADE, related_name='notes', verbose_name='Конкретный урок')
  student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='notes', verbose_name='Ученик')
  comment = models.CharField('Комментарий', max_length=256, blank=True, default='')
  last_modified = models.DateTimeField('Время', auto_now=True)
  
  def __str__(self):
    return f'{self.value} для {self.student} по {self.specific_lesson}'
  
  @property
  def homework(self):
    from .homework import Homework
    homework_qs: models.QuerySet[Homework] = self.specific_lesson.homeworks.filter(student=self.student)
    if homework_qs.exists():
      return homework_qs.first()
    return None
  
  class Meta:
    verbose_name = 'Оценка'
    verbose_name_plural = 'Оценки'