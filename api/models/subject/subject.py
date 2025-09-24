from django.db import models

from ..media import Media
from ..with_uuid import WithUUID

from .subject_type import SubjectType

class Subject(WithUUID):
  type = models.ForeignKey(SubjectType, on_delete=models.CASCADE, verbose_name='Тип', related_name='subjects')
  verbose_name = models.CharField('Читаемое название', blank=True, max_length=48)
  lang = models.CharField('Язык', max_length=2, blank=True)
  slug = models.SlugField('Слаг', max_length=64, db_index=True)

  manuals: models.Manager

  @property
  def image(self) -> str:
    return Media.append_prefix(f'subjects/{self.type.name}.png')

  @property
  def has_notes(self) -> bool:
    return self.type.has_notes

  def __str__(self):
    return f'{self.verbose_name if self.verbose_name else self.type} ({self.lang})'

  class Meta:
    ordering = ['lang', 'type__country', 'type__name']
    verbose_name = 'Название предмета'
    verbose_name_plural = 'Названия предметов'