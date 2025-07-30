from django.db import models
from uuid import uuid4

from .subject_type import SubjectType
from ..media import Media

class Subject(models.Model):
  id = models.UUIDField('id', default=uuid4, primary_key=True)
  type = models.ForeignKey(SubjectType, on_delete=models.CASCADE, verbose_name='Тип', related_name='subjects')
  verbose_name = models.CharField('Читаемое название', blank=True, max_length=48)
  lang = models.CharField('Язык', max_length=2, blank=True)
  
  manuals: models.Manager
  
  def __str__(self):
    return f'{self.verbose_name if self.verbose_name else self.type} ({self.lang})'
  
  @property
  def image(self):
    return Media.append_prefix(f'subjects/{self.type.name}.png')
  
  class Meta:
    ordering = ['lang', 'type__country', 'type__name']
    verbose_name = 'Название предмета'
    verbose_name_plural = 'Названия предметов'