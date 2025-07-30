from django.db import models
from uuid import uuid4

from .country import Country

class Region(models.Model):
  id = models.UUIDField('id', default=uuid4, primary_key=True)
  name = models.CharField('Название', max_length=32)
  country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, verbose_name='Страна', related_name='regions')
  
  cities: models.Manager
  
  def __str__(self):
    return f'{self.country}, {self.name}'
  
  class Meta:
    ordering = ['country', 'name']
    verbose_name = 'Регион'
    verbose_name_plural = 'Регионы'