from django.db import models

from ..subject.subject import Subject
from ..person.teacher import Teacher
from ..with_uuid import WithUUID
from .school import School

class Position(WithUUID):
  TYPES = {
    'HM': 'Директор',
    'HT': 'Завуч',
    'T': 'Учитель',
    'ET': 'Учитель младшего звена'
  }
  teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='work_places', verbose_name='Учитель')
  school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='staff', related_query_name='staff', verbose_name='Школа')
  subjects = models.ManyToManyField(Subject, verbose_name='Предметы', blank=True)
  type = models.CharField('Тип', choices=TYPES, max_length=2, default='T')
  is_manager = models.BooleanField('Является менеджером', default=False)

  def __str__(self):
    return f'{self.get_type_display()}: {self.teacher} в {self.school}'

  class Meta:
    ordering = ['school', 'type']
    verbose_name = 'Позиция'
    verbose_name_plural = 'Позиции'