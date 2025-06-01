from django.db import models
from uuid import uuid4

from ..school import Klass
from ..subject import SubjectName
from ..person import Teacher

class Lesson(models.Model):
  WEEKDAYS = {val: val for val in ('MO', 'TU', 'WE', 'TH', 'FR', 'SA', 'SU')}
  
  id = models.UUIDField('id', default=uuid4, primary_key=True)
  klass = models.ForeignKey(Klass, on_delete=models.CASCADE, related_name='timetable', verbose_name='Класс')
  subject_name = models.ForeignKey(SubjectName, on_delete=models.SET_NULL, null=True, default=None, verbose_name='Предмет')
  starting = models.TimeField('Начало')
  ending = models.TimeField('Конец')
  weekday = models.CharField('День недели', max_length=2, choices=WEEKDAYS)
  teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, default=None, verbose_name='Учитель')
  
  def __str__(self):
    return f'{self.klass} {self.subject_name}, начало в {self.starting}'
  
  class Meta:
    unique_together = ['klass', 'starting', 'weekday']
    verbose_name = 'Урок'
    verbose_name_plural = 'Уроки'