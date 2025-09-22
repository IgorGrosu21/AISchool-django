from django.db import models

from ..country.country import Country
from ..with_uuid import WithUUID

class SubjectType(WithUUID):
  name = models.CharField('Название', max_length=32)
  country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, verbose_name='Страна', related_name='subject_types')
  has_notes = models.BooleanField('Имеет оценки')
  
  subjects: models.Manager
  
  def __str__(self):
    return self.name
  
  class Meta:
    ordering = ['country', 'name']
    verbose_name = 'Тип предмета'
    verbose_name_plural = 'Типы предметов'