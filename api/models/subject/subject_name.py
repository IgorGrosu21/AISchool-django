from django.db import models
from uuid import uuid4

from .subject_type import SubjectType

class SubjectName(models.Model):
  id = models.UUIDField('id', default=uuid4, primary_key=True)
  type = models.ForeignKey(SubjectType, on_delete=models.SET_NULL, null=True, verbose_name='Тип', related_name='subject_names')
  verbose_name = models.CharField('Читаемое название', default='', blank=True, max_length=48)
  lang = models.CharField('Язык', max_length=2, blank=True)
  
  def __str__(self):
    return f'{self.verbose_name if self.verbose_name else self.type} ({self.lang})'
  
  class Meta:
    ordering = ['lang', 'type__country', 'type__name']
    verbose_name = 'Название предмета'
    verbose_name_plural = 'Названия предметов'