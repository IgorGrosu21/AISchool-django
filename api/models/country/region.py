from django.db import models

from ..with_uuid import WithUUID
from .country import Country

class Region(WithUUID):
  name = models.CharField('Название', max_length=32)
  country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, verbose_name='Страна', related_name='regions')
  slug = models.SlugField('Слаг', max_length=64, db_index=True)
  
  cities: models.Manager
  
  def __str__(self):
    return f'{self.country}, {self.name}'
  
  class Meta:
    ordering = ['country', 'name']
    verbose_name = 'Регион'
    verbose_name_plural = 'Регионы'