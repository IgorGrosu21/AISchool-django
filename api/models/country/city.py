from django.db import models
from uuid import uuid4

from .region import Region

class City(models.Model):
  id = models.UUIDField('id', default=uuid4, primary_key=True)
  name = models.CharField('Название', max_length=32)
  region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, verbose_name='Регион', related_name='cities')
  
  def __str__(self):
    return f'{self.region}, {self.name}'
  
  class Meta:
    ordering = ['region__country', 'region', 'name']
    verbose_name = 'Город'
    verbose_name_plural = 'Города'