from django.db import models
from uuid import uuid4

from ..subject import SubjectName

class Position(models.Model):
  TYPES = {
    'HM': 'Директор',
    'HT': 'Завуч',
    'T': 'Учитель',
    'ET': 'Учитель младшего звена'
  }
  
  id = models.UUIDField('id', default=uuid4, primary_key=True)
  teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE, related_name='work_places', verbose_name='Учитель')
  school = models.ForeignKey('School', on_delete=models.CASCADE, related_name='staff', related_query_name='staff', verbose_name='Школа')
  subject_names = models.ManyToManyField(SubjectName, related_name='teachers', verbose_name='Предметы', blank=True)
  type = models.CharField('Тип', choices=TYPES, max_length=2, default='T')
  is_manager = models.BooleanField('Является менеджером', default=False)
  
  def __str__(self):
    return f'{self.get_type_display()}: {self.teacher} в {self.school}'
  
  class Meta:
    ordering = ['school', 'type']
    verbose_name = 'Позиция'
    verbose_name_plural = 'Позиции'