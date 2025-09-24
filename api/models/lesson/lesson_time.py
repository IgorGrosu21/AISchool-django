from django.db import models

from ..school.school import School
from ..with_uuid import WithUUID

class LessonTime(WithUUID):
  WEEKDAYS = {val: val for val in ('MO', 'TU', 'WE', 'TH', 'FR', 'SA', 'SU')}
  school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='timetable', verbose_name='Класс')
  starting = models.TimeField('Начало')
  ending = models.TimeField('Конец')
  order = models.SmallIntegerField('Порядок')
  weekday = models.CharField('День недели', max_length=2, choices=WEEKDAYS)

  lessons: models.Manager

  def __str__(self):
    return f'{self.school}, начало в {self.starting} ({self.weekday})'

  class Meta:
    ordering = ['school', 'weekday', 'order']
    verbose_name = 'Время урока'
    verbose_name_plural = 'Время уроков'