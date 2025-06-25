from django.db import models
from uuid import uuid4

from ..school import School

class LessonTime(models.Model):
  WEEKDAYS = {val: val for val in ('MO', 'TU', 'WE', 'TH', 'FR', 'SA', 'SU')}
  
  id = models.UUIDField('id', default=uuid4, primary_key=True)
  school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='timetable', verbose_name='Класс')
  starting = models.TimeField('Начало')
  ending = models.TimeField('Конец')
  order = models.SmallIntegerField('Порядок')
  weekday = models.CharField('День недели', max_length=2, choices=WEEKDAYS)
  
  def __str__(self):
    return f'{self.school}, начало в {self.starting} ({self.weekday})'
  
  class Meta:
    ordering = ['school', 'weekday', 'starting']
    verbose_name = 'Время урока'
    verbose_name_plural = 'Время уроков'